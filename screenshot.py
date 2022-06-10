import base64
import io
import random
from datetime import datetime, timezone, timedelta

import qrcode
from PIL import Image
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from constant import logo_base64, nil_base64, data_uri_png, data_uri_html, qrcode_url, time_format, time_format2, \
	vacc_date


def generate_akm_qrcode(token=None):
	logo = Image.open(io.BytesIO(base64.decodebytes(bytes(logo_base64, 'utf-8'))))
	if not token:
		token = random.randbytes(16).hex()
	url_token = qrcode_url.format(token)
	qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_H, border=0, box_size=10)
	qr.add_data(url_token)
	qr.make(fit=True)
	code = qr.make_image(fill_color='#5cb83d', back_color='white').convert('RGBA')
	img = Image.new('RGBA', code.size, (0, 0, 0, 0))
	size = (int(img.size[0] / 3.5), int(img.size[1] / 3.5))
	pos = (int(img.size[0] * 1.25 / 3.5), int(img.size[1] * 1.25 / 3.5))
	logo = logo.resize(size, Image.Resampling.BILINEAR)
	img.paste(logo, pos)
	img = Image.alpha_composite(code, img)
	buffered = io.BytesIO()
	img.save(buffered, format='png')
	return data_uri_png + base64.b64encode(buffered.getvalue()).decode('utf-8')


def generate_akm_html(real_name='', time=None):
	with open('.\\html\\akm.html', 'r+', encoding='utf-8') as f:
		text = f.read()
	soup = bs(text, 'html.parser')
	with open('.\\html\\akm.css', 'r+', encoding='utf-8') as f:
		css = f.read()
		soup.link.decompose()
		style = soup.new_tag('style')
		style.string = css
		soup.meta.append(style)
	soup.find(id='auto-report-akm-qrcode')['src'] = generate_akm_qrcode()
	if real_name:
		soup.find(id='auto-report-real-name').string = real_name
	if time:
		soup.find(id='auto-report-date-time').string = time.strftime(time_format)
		vacc_delta = time - datetime.strptime(vacc_date, time_format).astimezone(timezone(timedelta(hours=+8)))
		soup.find(id='auto-report-vacc-past').string = str(vacc_delta.days)
	return soup.__str__()


def generate_xck_html(mobile_phone='', time=None):
	with open('.\\html\\xck.html', 'r+', encoding='utf-8') as f:
		text = f.read()
	soup = bs(text, 'html.parser')
	with open('.\\html\\xck.css', 'r+', encoding='utf-8') as f:
		css = f.read()
		soup.link.decompose()
		style = soup.new_tag('style')
		style.string = css
		soup.meta.append(style)
	if mobile_phone:
		soup.find(id='auto-report-mobile-phone').string = mobile_phone
	if time:
		soup.find(id='auto-report-date-time-2').string = time.strftime(time_format2)
	return soup.__str__()


def generate_na_html(real_name='', na_id='', collect_agency='', collect_time=None, test_agency='', test_time=None):
	if not na_id:
		return ''
	with open('.\\html\\na.html', 'r+', encoding='utf-8') as f:
		text = f.read()
	soup = bs(text, 'html.parser')
	with open('.\\html\\na.css', 'r+', encoding='utf-8') as f:
		css = f.read()
		soup.link.decompose()
		style = soup.new_tag('style')
		style.string = css
		soup.meta.append(style)
	if real_name:
		soup.find(id='auto-report-real-name').string = '*' * (len(real_name) - 1) + real_name[-1:]
	if na_id:
		soup.find(id='auto-report-id').string = na_id[:4] + '*' * 10 + na_id[-4:]
	if collect_agency:
		soup.find(id='auto-report-collect-agency').string = collect_agency
	if test_agency:
		soup.find(id='auto-report-test-agency').string = test_agency
	if collect_time and test_time:
		soup.find(id='auto-report-collect-time').string = collect_time.strftime(time_format)
		soup.find(id='auto-report-test-time').string = test_time.strftime(time_format)
	# soup.find(id='auto-report-nuac-past').string = str((now - test_time).days)
	return soup.__str__()


def generate_screenshot(real_name='', mobile_phone='', na_id=''):
	now = datetime.now(tz=timezone(timedelta(hours=+8)))
	random.seed(int(now.strftime('%W')))
	time1 = now - timedelta(seconds=random.randint(120, 179))
	time2 = now - timedelta(seconds=random.randint(60, 119))
	time3 = now.replace(hour=12, minute=0, second=0) + timedelta(days=-2, seconds=random.randint(0, 7199))
	time4 = now.replace(hour=2, minute=0, second=0) + timedelta(days=-1, seconds=random.randint(0, 7199))
	firefox_options = webdriver.FirefoxOptions()
	firefox_options.headless = True
	firefox_driver = webdriver.Firefox(options=firefox_options)

	akm_html = generate_akm_html(real_name=real_name, time=time1)
	akm_html_base64 = base64.b64encode(akm_html.encode('utf-8')).decode()
	firefox_driver.get(data_uri_html + akm_html_base64)
	firefox_driver.set_window_rect(width=640, height=1280)
	akm_screenshot_base64 = data_uri_png + firefox_driver.get_full_page_screenshot_as_base64()
	firefox_driver.save_full_page_screenshot('akm.png')

	xck_html = generate_xck_html(mobile_phone=(mobile_phone[:3] + '****' + mobile_phone[7:11]), time=time2)
	xck_html_base64 = base64.b64encode(xck_html.encode('utf-8')).decode()
	firefox_driver.get(data_uri_html + xck_html_base64)
	firefox_driver.set_window_rect(width=400, height=800)
	xck_screenshot_base64 = data_uri_png + firefox_driver.get_full_page_screenshot_as_base64()
	firefox_driver.save_full_page_screenshot('xck.png')

	if na_id and 2 <= now.weekday() <= 5:
		na_html = generate_na_html(real_name=real_name, na_id=na_id, collect_agency='', collect_time=time3,
		                           test_agency='', test_time=time4)
		na_html_base64 = base64.b64encode(na_html.encode('utf-8')).decode()
		firefox_driver.get(data_uri_html + na_html_base64)
		firefox_driver.set_window_rect(width=640, height=1280)
		na_screenshot_base64 = data_uri_png + firefox_driver.get_full_page_screenshot_as_base64()
		firefox_driver.save_full_page_screenshot('na.png')
	else:
		na_screenshot_base64 = data_uri_png + nil_base64

	return akm_screenshot_base64, xck_screenshot_base64, na_screenshot_base64


generate_screenshot('徐盛榕', '18745058660', '230102200201092114')
