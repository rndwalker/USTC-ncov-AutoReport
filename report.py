import argparse
import json
import re
import traceback

from bs4 import BeautifulSoup

from ustclogin2 import Login


def login(username, password):
	token = ''
	login = Login(username, password, 'https://weixine.ustc.edu.cn/2020/caslogin')
	if login.login():
		data = login.result.text
		data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
		soup = BeautifulSoup(data, 'html.parser')
		token = soup.find('input', {'name': '_token'})['value']
	return token, login


def report(username, password, daily, screenshot, cross_campus, data_path, max_tries, real_name, mobile_phone):
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
	}
	cross_data = {"return_college[]": [
		"中校区",
		"西校区",
		"南校区",
		"北校区",
		"东校区"
	], "reason": "实验、自习", "t": "3"}
	home_url = 'https://weixine.ustc.edu.cn/2020'
	daily_url = 'https://weixine.ustc.edu.cn/2020/daliy_report'
	cross_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3'
	cross_return_url = 'https://weixine.ustc.edu.cn/2020/apply_total?t=d'
	cross_post_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/post'
	success_alert = '上报成功'
	time_diff_pattern = re.compile('((0|[1-9]\\d*)(年|月|周|星期|日|天|小时|时|分钟|分|秒))+')
	ret=0
	# Login
	for tries in range(max_tries):
		try:
			token, login = login(username, password, max_tries)
			if token and login:
				break
		except:
			print('* Error: Login: Get Token Failed in run {0}, detail as follows:'.format(tries))
			print(traceback.format_exc())
			continue
	if not token or not login:
		print('*** FATAL ERROR\n*** Login Failed!\n*** Script Failed!\n')
		return 2
	headers |= {'cookie', 'PHPSESSID=' + login.cookies.get('PHPSESSID') + ';XSRF-TOKEN=' + login.cookies.get(
		'XSRF-TOKEN') + ';laravel_session=' + login.cookies.get('laravel_session')}
	# Read JSON
	try:
		with open(data_path, 'r+', encoding='utf-8') as f:
			data = json.loads(f.read())
			if not data:
				raise RuntimeError("* Error: Read JSON: Empty json found in {}!".format(data_path))
			data |= {'_token', token}
			cross_data |= {'_token', token}
	except:
		print('*** FATAL ERROR\n*** Reading JSON Failed!\n*** Script Failed!\n')
		print(traceback.format_exc())
		return 4
	# Getting Previous Daily Report Data
	try:
		get = login.session.get(home_url, headers=headers)
		soup = BeautifulSoup(get.text, 'html.parser')
		jinji_lxr = soup.find('input', {'name': 'jinji_lxr'})['value']
		jinji_guanxi = soup.find('input', {'name': 'jinji_guanxi'})['value']
		jiji_mobile = soup.find('input', {'name': 'jiji_mobile'})['value']
		dorm_building = soup.find('input', {'name': 'dorm_building'})['value']
		dorm = soup.find('input', {'name': 'dorm'})['value']
		if not real_name:
			real_name = jinji_guanxi
		if not mobile_phone:
			mobile_phone = jiji_mobile
		data |= {'jinji_lxr': jinji_lxr, 'jinji_guanxi': jinji_guanxi, 'jiji_mobile': jiji_mobile,
		         'dorm_building': dorm_building, 'dorm': dorm}
	except:
		print('* Warning: Daily Report: Getting Previous Report Data Failed, using default JSON:')
		print(traceback.format_exc())
	# Daily Report
	if not daily:
		print('Skipping Daily Report...')
	else:
		ret |= 8
		for tries in range(max_tries):
			try:
				post = login.session.post(daily_url, data=data, headers=headers)
				soup = BeautifulSoup(post.text, 'html.parser')
				alert = soup.find('p', {'class': 'alert alert-success'})
				if alert.text.find(success_alert) != -1:
					print('Got Daily Report Success Alert!')
					ret &= -9
				else:
					print("* Warning: Daily Report: Failed to get success alert...")
				if time_diff_pattern.search(alert.text):
					time_diff = time_diff_pattern.search(alert.text).group()
					print('Last report: {0} before.'.format(time_diff))
					ret &= -9
				else:
					print("* Warning: Daily Report: Failed to get last report time...")
				if not ret:
					print('Daily Report Successful!')
					break
				else:
					print(
						'* Error: Daily Report: Run {0} Finished but Failed to get response from alert, retrying...'.format(
							tries))
			except:
				print('* Error: Daily Report: Run {0} Failed, detail as follows:'.format(tries))
				print(traceback.format_exc())
				continue
		if ret & 8:
			print('* FATAL ERROR\n* Daily Report Failed!\n* Continuing anyway...\n')
	# Cross-campus Report
	ret = ret | 16
	for tries in range(max_tries):
		try:
			get = login.session.get(cross_url, headers=headers)
			soup = BeautifulSoup(get.text, 'html.parser')
			start_date = soup.find('input', {'id': 'start_date'})['value']
			end_date = soup.find('input', {'id': 'end_date'})['value']
			cross_data['start_date'] = start_date
			cross_data['end_date'] = end_date
			post = login.session.post(cross_post_url, data=cross_data, headers=headers)
			if post.url == cross_return_url:
				print('Cross-campus Report Successful! Until: {0}'.format(end_date))
				ret = ret & -17
				break
			print('* Error: Cross-campus Report: Run {0} Finished but Failed to leave a record, retrying...'.format(
				tries))
		except:
			print('* Error: Cross-campus Report: Run {0} Failed, detail as follows:'.format(tries))
			print(traceback.format_exc())
			continue
	if ret & 16:
		print('* FATAL ERROR\n* Cross-campus Report Failed!\n')
	return ret


if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='URC nCov auto report script.', epilog='Men cannot live free, but he can die free.')
	parser.add_argument('username', help='your student number', type=str)
	parser.add_argument('password', help='your CAS password', type=str)
	parser.add_argument(
		'-d', '--daily', help='runs Daily Report', action='store_true')
	parser.add_argument(
		'-s', '--screenshot', help='runs Screenshot Generation', action='store_true')
	parser.add_argument(
		'-c', '--cross_campus', help='runs Cross-campus Report', action='store_true')
	parser.add_argument(
		'-p', '--data_path', help='path to your own data.json', type=str, default='./data.json')
	parser.add_argument(
		'-t', '--max_tries', help='max tries as in reports', type=int, default=5)
	parser.add_argument(
		'-n', '--real_name',
		help='specifies your real name to generate screenshots rather than reading from previous report', type=str)
	parser.add_argument(
		'-m', '--mobile_phone',
		help='specifies your mobile phone to generate screenshots rather than reading from previous report', type=str)
	args = parser.parse_args()
	result = report(args.username, args.password, args.daily, args.screenshot, args.cross_campus, args.data_path,
	                args.max_tries, args.real_name, args.mobile_phone)
	exit(result)
