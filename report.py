import argparse
import json
import re
import traceback
from datetime import datetime, timezone, timedelta
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup as bs

from constant import data as const_data, headers as const_headers, cross_data as const_cross_data
from constant import login_url,caslogin_url,home_url, daily_url, cross_post_url,time_format


def get_passport(username, password, session, service):
	get = session.get(login_url+'?service=' + service, headers=const_headers)
	soup = bs(get.text, 'html.parser')
	cas_lt = soup.find('input', {'name': 'CAS_LT'})['value']
	data = {
		'model': 'uplogin.jsp',
		'service': unquote(service),
		'warn': '',
		'showCode': '',
		'username': username,
		'password': str(password),
		'button': '',
		'CAS_LT': cas_lt,
		'LT': ''
	}
	return session.post(login_url, data=data, headers=const_headers)


def get_token(username, password):
	token = ''
	session = requests.Session()
	post = get_passport(username, password, session, caslogin_url)
	if post.url != login_url:
		soup = bs(post.text, 'html.parser')
		token = soup.find('input', {'name': '_token'})['value']
	return token, session


def read_info(session, headers):
	get = session.get(home_url, headers=headers)
	soup = bs(get.text, 'html.parser')
	# noinspection SpellCheckingInspection
	jinji_lxr = soup.find('input', {'name': 'jinji_lxr'})['value']
	# noinspection SpellCheckingInspection
	jinji_guanxi = soup.find('input', {'name': 'jinji_guanxi'})['value']
	# noinspection SpellCheckingInspection
	jiji_mobile = soup.find('input', {'name': 'jiji_mobile'})['value']
	dorm_building = soup.find('input', {'name': 'dorm_building'})['value']
	dorm = soup.find('input', {'name': 'dorm'})['value']
	# noinspection SpellCheckingInspection
	read_data = {'jinji_lxr': jinji_lxr, 'jinji_guanxi': jinji_guanxi, 'jiji_mobile': jiji_mobile,
	             'dorm_building': dorm_building, 'dorm': dorm}
	return read_data, jinji_lxr, jiji_mobile


def daily_report(session, data, headers):
	post = session.post(daily_url, data=data, headers=headers)
	soup = bs(post.text, 'html.parser')
	alert = soup.find('p', {'class': 'alert alert-success'}).text
	if '上报成功' in alert:
		print('Got Daily Report Success Alert!')
	else:
		print('* Warning: Daily Report: Failed to get success alert...')
	search_result = re.compile('((0|[1-9]\\d*)(年|月|周|星期|日|天|小时|时|分钟|分|秒))+').search(alert)
	if search_result:
		time_diff = search_result.group().replace('年', ' year(s) ').replace('月', ' month(s) ') \
			.replace('周', ' week(s) ').replace('星期', ' week(s) ').replace('日', ' day(s) ') \
			.replace('天', ' day(s) ').replace('小时', ' hour(s) ').replace('时', ' hour(s) ') \
			.replace('分钟', ' minute(s) ').replace('分', ' minute(s) ').replace('秒', ' second(s)')
		print('Daily Report Successful!\nLast report: {} before.'.format(time_diff))
		return True
	else:
		print('* Error: Daily Report: Finished but failed to get last report time, retrying...')
		return False


def screenshot_upload(real_name, mobile_phone):
	# generate_akm()
	# generate_xcm()
	# generate_hs()
	# pic_upload()
	pass


def cross_campus_report(session, headers, cross_data):
	start = datetime.now(tz=timezone(timedelta(hours=+8)))
	if start.hour >= 20:
		end = start + timedelta(days=1)
	else:
		end = start.replace(hour=23, minute=59, second=59)
	start_date = start.strftime(time_format)
	end_date = end.strftime(time_format)
	cross_data['start_date'] = start_date
	cross_data['end_date'] = end_date
	post = session.post(cross_post_url, cross_data, headers=headers)
	if start_date in post.text and end_date in post.text:
		print('Cross-campus Report Successful!\n{} to {}.'.format(start_date, end_date))
		return True
	print('* Error: Cross-campus Report: Finished but Failed to leave a record, retrying...')
	return False


def report(username, password, daily, screenshot, cross_campus, max_tries, real_name, mobile_phone, na_id):
	ret = 0

	# Login
	token, session = '', None
	for tries in range(max_tries):
		try:
			token, session = get_token(username, password)
			if token and session:
				break
		except:
			print('* Error: Login: Get Token run {} throws error, detail as follows:'.format(tries))
			print(traceback.format_exc())
			continue
	if not token or not session:
		print('*** FATAL ERROR\n*** Login Failed!\n*** Script Failed!')
		return 3
	# noinspection SpellCheckingInspection
	cookie = 'PHPSESSID=' + session.cookies.get('PHPSESSID') + ';XSRF-TOKEN=' + session.cookies.get(
		'XSRF-TOKEN') + ';laravel_session=' + session.cookies.get('laravel_session')
	headers = const_headers | {'cookie': cookie}
	data=const_data|{'_token': token}
	cross_data = const_cross_data | {'_token': token}

	# Reading information from previous report
	read_data, read_name, read_mobile = {}, '', ''
	for tries in range(max_tries):
		try:
			read_data, read_name, read_mobile = read_info(session, headers)
			if read_data and read_name and read_mobile:
				break
		except:
			print('* Error: Reading Info: Run {} throws error, detail as follows:'.format(tries))
			print(traceback.format_exc())
			continue
	if read_data:
		data |= read_data
	else:
		print('* Warning: Daily Report: Reading previous report info failed, using default JSON.')
	if real_name:
		print('Using specified real name.')
	else:
		if read_name:
			print('Using real name from previous report...')
			real_name = read_name
		else:
			print('* Caution: Using masked real name for Screenshot Generation; NO WARRANTIES!')
			real_name = '***'
	if mobile_phone:
		print('Using specified mobile phone.')
	else:
		if read_mobile:
			print('Using mobile phone from previous report...')
			mobile_phone = read_mobile[:3] + '****' + read_mobile[7:11]
		else:
			print('* Caution: Using fake mobile phone for Screenshot Generation; NO WARRANTIES!')
			mobile_phone = '198****0817'

	# Daily Report
	if not daily:
		print('Skipping Daily Report...')
	else:
		print('Running Daily Report...')
		ret |= 4
		for tries in range(max_tries):
			try:
				if daily_report(session, data, headers):
					ret &= -5
					break
			except:
				print('* Error: Daily Report: Run {} throws error, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if ret & 4:
			print('*** FATAL ERROR\n*** Daily Report failed!\n*** Continuing anyway...')

	# Screenshot Upload
	if 1 or not screenshot:
		print('Skipping Screenshot Upload...')
	else:
		print('Running Screenshot Upload...')
		try:
			# screenshot_upload(real_name, mobile_phone)
			# WIP
			pass
		except:
			print('* Error: Screenshot Upload throws error, detail as follows:')
			print(traceback.format_exc())

	# Cross-campus Report
	if not cross_campus:
		print('Skipping Cross-campus Report...')
	else:
		print('Running Cross-campus Report...')
		ret |= 16
		for tries in range(max_tries):
			try:
				if cross_campus_report(session, headers, cross_data):
					ret &= -17
					break
			except:
				print('* Error: Cross-campus: Run {} throws error, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if ret & 16:
			print('*** FATAL ERROR\n*** Cross-campus Report failed!')

	return ret


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='URC nCov auto report script.',
	                                 epilog='Man cannot live free, but he can die free.')
	parser.add_argument('username', help='your student number', type=str)
	parser.add_argument('password', help='your CAS password', type=str)
	parser.add_argument(
		'-d', '--daily', help='runs Daily Report', action='store_true')
	parser.add_argument(
		'-s', '--screenshot', help='runs Screenshot Generation & Upload', action='store_true')
	parser.add_argument(
		'-c', '--cross_campus', help='runs Cross-campus Report', action='store_true')
	parser.add_argument(
		'-t', '--max_tries', help='max tries as in reports', type=int, default=5)
	parser.add_argument(
		'-n', '--real_name',
		help='specifies your real name to generate screenshots rather than reading from previous report', type=str)
	parser.add_argument(
		'-m', '--mobile_phone',
		help='specifies your mobile phone to generate screenshots rather than reading from previous report', type=str)
	parser.add_argument(
		'-i', '--na_id',
		help='your ID; only generates and uploads nucleic acid report when specified (NO WARRANTIES)', type=str)
	args = parser.parse_args()
	result = report(args.username, args.password, args.daily, args.screenshot, args.cross_campus,
	                args.max_tries, args.real_name, args.mobile_phone, args.na_id)
	exit(result)
