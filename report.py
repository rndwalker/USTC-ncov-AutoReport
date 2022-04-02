import argparse
import datetime
import json
import re
import traceback

import pytz
from bs4 import BeautifulSoup

from ustclogin2 import Login


class Report(object):
	def __init__(self, username, password, data_path):
		self.username = username
		self.password = password
		self.data_path = data_path

	def report(self, max_tries=10):
		# Login
		token = ''
		for tries in range(max_tries):
			try:
				login = Login(self.username, self.password, 'https://weixine.ustc.edu.cn/2020/caslogin')
				if login.login():
					data = login.result.text
					data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
					soup = BeautifulSoup(data, 'html.parser')
					token = soup.find('input', {'name': '_token'})['value']
					if token != '':
						break
			except:
				print('* Error: Login: Get Token Failed in run {0}, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if not token:
			print('*** FATAL ERROR\n*** Login Failed!\n*** Script Failed!\n')
			return -1
		# Constant Values
		headers = {
			'authority': 'weixine.ustc.edu.cn',
			'origin': 'https://weixine.ustc.edu.cn',
			'upgrade-insecure-requests': '1',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'referer': 'https://weixine.ustc.edu.cn/2020/',
			'accept-language': 'zh-CN,zh;q=0.9',
			'Connection': 'close',
			'cookie': 'PHPSESSID=' + login.cookies.get('PHPSESSID') + ';XSRF-TOKEN=' + login.cookies.get(
				'XSRF-TOKEN') + ';laravel_session=' + login.cookies.get('laravel_session')
		}
		home_url = 'https://weixine.ustc.edu.cn/2020'
		daily_url = 'https://weixine.ustc.edu.cn/2020/daliy_report'
		cross_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3'
		cross_return_url = 'https://weixine.ustc.edu.cn/2020/apply_total?t=d'
		cross_post_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/post'
		date_pattern = re.compile(
			'202[0-9]-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}')
		alert_attr = {'style': 'position: relative; top: 5px; color: #666;'}
		# Read JSON
		data = None
		with open(self.data_path, 'r+', encoding='utf-8') as f:
			data = json.loads(f.read())
			data['_token'] = token
		# if self.cont_name:
		# 	data['jinji_lxr'] = self.cont_name
		# if self.cont_rel:
		# 	data['jinji_guanxi'] = self.cont_rel
		# if self.cont_num:
		# 	data['jiji_mobile'] = self.cont_num
		if not data:
			print('*** FATAL ERROR\n*** Reading JSON Failed!\n*** Script Failed!\n')
			return False
		# Getting Previous Daily Report Data
		try:
			get = login.session.get(home_url, headers=headers)
			soup = BeautifulSoup(get.text, 'html.parser')
			alert = soup.find('span', alert_attr)
			if date_pattern.search(alert.text):
				date = date_pattern.search(alert.text).group()
				print('Last report: ' + date)
			jinji_lxr = soup.find('input', {'name': 'jinji_lxr'})['value']
			jinji_guanxi = soup.find('input', {'name': 'jinji_guanxi'})['value']
			jiji_mobile = soup.find('input', {'name': 'jiji_mobile'})['value']
			dorm_building = soup.find('input', {'name': 'dorm_building'})['value']
			dorm = soup.find('input', {'name': 'dorm'})['value']
			data['jinji_lxr'] = jinji_lxr
			data['jinji_guanxi'] = jinji_guanxi
			data['jiji_mobile'] = jiji_mobile
			data['dorm_building'] = dorm_building
			data['dorm'] = dorm
		except:
			print('* Warning: Daily Report: Getting Previous Report Data Failed, using default JSON:')
			print(traceback.format_exc())

		# Daily Report
		ret = 2
		for tries in range(max_tries):
			try:
				login.session.post(daily_url, data=data, headers=headers)
				get = login.session.get(home_url, headers=headers)
				soup = BeautifulSoup(get.text, 'html.parser')
				alert = soup.find('span', alert_attr)
				if date_pattern.search(alert.text):
					date = date_pattern.search(alert.text).group()
					print('Latest report: ' + date)
					date = date + ' +0800'
					report_time = datetime.datetime.strptime(
						date, '%Y-%m-%d %H:%M:%S %z')
					time_now = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
					time_diff = time_now - report_time
					print('{} second(s) before.'.format(time_diff.seconds))
					if time_diff.seconds < 120:
						print('Daily Report Successful!')
						ret = 0
						break
					print('* Error: Daily Report: Run {0} Finished but Failed to leave a record, retrying...'.format(
						tries))
					break
				print(
					'* Error: Daily Report: Run {0} Finished but Failed to get response from alert, retrying...'.format(
						tries))
			except:
				print('* Error: Daily Report: Run {0} Failed, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if ret:
			print('* FATAL ERROR\n* Daily Report Failed!\n* Trying Cross-campus Report anyway...\n')

		# Cross-campus Report
		ret = ret | 4
		for tries in range(max_tries):
			try:
				get = login.session.get(cross_url, headers=headers)
				# get.text = get.text.encode('ascii', 'ignore').decode('utf-8', 'ignore')
				soup = BeautifulSoup(get.text, 'html.parser')
				start_date = soup.find('input', {'id': 'start_date'})['value']
				end_date = soup.find('input', {'id': 'end_date'})['value']
				data['start_date'] = start_date
				data['end_date'] = end_date
				post = login.session.post(cross_post_url, data=data, headers=headers)
				if post.url == cross_return_url:
					print('Cross-campus Report Successful! Until: {0}'.format(end_date))
					ret = ret & -5
					break
				print('* Error: Cross-campus Report: Run {0} Finished but Failed to leave a record, retrying...'.format(
					tries))
			except:
				print('* Error: Cross-campus Report: Run {0} Failed, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if ret & 4:
			print('* FATAL ERROR\n* Cross-campus Report Failed!\n')

		return -ret


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='URC nCov auto report script.')
	parser.add_argument('username', help='your student number', type=str)
	parser.add_argument('password', help='your CAS password', type=str)
	parser.add_argument(
		'--data_path', help='path to your own data used for post method', type=str, default='data.json')
	parser.add_argument(
		'--max_tries', help='max tries as in Fixed Daily Report & Cross-campus Report', type=int, default=10)
	args = parser.parse_args()
	autoreporter = Report(username=args.username, password=args.password, data_path=args.data_path)
	exit(autoreporter.report())
