from io import BytesIO
from urllib.parse import unquote

import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image
from bs4 import BeautifulSoup

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}


class Login:
	def __init__(self, stuid, password, service):
		self.stuid = stuid
		self.password = password
		self.service = service

	def get_LT(self):
		text = self.session.get('https://passport.ustc.edu.cn/validatecode.jsp?type=login', stream=True).content
		image = Image.open(BytesIO(text))
		image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
		kernel = np.ones((3, 3), np.uint8)
		image = cv2.dilate(image, kernel, iterations=1)
		image = cv2.erode(image, kernel, iterations=1)
		return pytesseract.image_to_string(Image.fromarray(image))[:4]

	def passport(self):
		data = self.session.get('https://passport.ustc.edu.cn/login?service=' + self.service, headers=headers)
		data = data.text
		data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
		soup = BeautifulSoup(data, 'html.parser')
		CAS_LT = soup.find("input", {"name": "CAS_LT"})['value']
		LT = self.get_LT()
		data = {
			'model': 'uplogin.jsp',
			'service': unquote(self.service),
			'warn': '',
			'showCode': '1',
			'username': self.stuid,
			'password': str(self.password),
			'button': '',
			'CAS_LT': CAS_LT,
			'LT': LT
		}
		self.result = self.session.post('https://passport.ustc.edu.cn/login', data=data, headers=headers)

	def login(self):
		self.session = requests.Session()
		loginsuccess = False
		retrycount = 5
		while (not loginsuccess) and retrycount:
			self.passport()
			self.cookies = self.session.cookies
			retrycount = retrycount - 1
			if self.result.url == 'https://passport.ustc.edu.cn/login':
				print("Login Failed! Retry...")
			else:
				print("Login Successful!")
				loginsuccess = True
		return loginsuccess
