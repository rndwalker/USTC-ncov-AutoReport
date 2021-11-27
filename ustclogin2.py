from bs4 import BeautifulSoup
import requests


class Login:
    def __init__(self, username, password, origin, service, exam):
        self.username = username
        self.password = password
        self.origin = origin
        self.service = service
        self.exam = exam

    def passport(self):
        data = self.session.get(
            'https://passport.ustc.edu.cn/login?service='+self.service)
        data = data.text
        data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
        soup = BeautifulSoup(data, 'html.parser')
        CAS_LT = soup.find("input", {"name": "CAS_LT"})['value']
        self.session.get(
            'https://passport.ustc.edu.cn/validatecode.jsp?type=login', stream=True)
        data = {
            'model': 'uplogin.jsp',
            'service': self.service,
            'warn': '',
            'showCode': '0',
            'username': self.username,
            'password': str(self.password),
            'button': '',
            'CAS_LT': CAS_LT,
            'LT': ''
        }
        self.session.post('https://passport.ustc.edu.cn/login', data=data)

    def login(self):
        self.session = requests.Session()
        loginsuccess = False
        retrycount = 5
        while (not loginsuccess) and retrycount:
            self.passport()
            self.cookies = self.session.cookies
            self.result = self.session.get(self.origin)
            retrycount = retrycount - 1
            if self.result.url != self.exam:
                print("Login Failed! Retry...")
            else:
                print("Login Successful!")
                loginsuccess = True
        return loginsuccess

