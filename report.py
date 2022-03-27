import datetime
import re
import argparse
from bs4 import BeautifulSoup
import json
import pytz
from ustclogin2 import Login


class Report(object):
    def __init__(self, username, password, data_path, cont_name, cont_rel, cont_num):
        self.username = username
        self.password = password
        self.data_path = data_path
        self.cont_name = cont_name
        self.cont_rel = cont_rel
        self.cont_num = cont_num

    def report(self):
        login = Login(self.username, self.password, 'https://weixine.ustc.edu.cn/2020',
                      'https://weixine.ustc.edu.cn/2020/caslogin', 'https://weixine.ustc.edu.cn/2020/home')
        if login.login():
            data = login.result.text
            data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
            soup = BeautifulSoup(data, 'html.parser')
            token = soup.find("input", {"name": "_token"})['value']

            with open(self.data_path, "r+", encoding='utf-8') as f:
                data = f.read()
                data = json.loads(data)
                data["_token"] = token
                if self.cont_name:
                    data["jinji_lxr"] = self.cont_name
                if self.cont_rel:
                    data["jinji_guanxi"] = self.cont_rel
                if self.cont_num:
                    data["jiji_mobile"] = self.cont_num
            headers = {
                'authority': 'weixine.ustc.edu.cn',
                'origin': 'https://weixine.ustc.edu.cn',
                'upgrade-insecure-requests': '1',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'referer': 'https://weixine.ustc.edu.cn/2020/',
                'accept-language': 'zh-CN,zh;q=0.9',
                'Connection': 'close',
                'cookie': "PHPSESSID=" + login.cookies.get("PHPSESSID") + ";XSRF-TOKEN=" + login.cookies.get(
                    "XSRF-TOKEN") + ";laravel_session=" + login.cookies.get("laravel_session"),
            }

            url = "https://weixine.ustc.edu.cn/2020/daliy_report"
            resp = login.session.post(url, data=data, headers=headers)
            data = login.session.get("https://weixine.ustc.edu.cn/2020").text
            soup = BeautifulSoup(data, 'html.parser')
            pattern = re.compile(
                "202[0-9]-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}")
            token = soup.find(
                "span", {"style": "position: relative; top: 5px; color: #666;"})
            flag = False
            if pattern.search(token.text) is not None:
                date = pattern.search(token.text).group()
                print("Latest report: " + date)
                date = date + " +0800"
                reporttime = datetime.datetime.strptime(
                    date, "%Y-%m-%d %H:%M:%S %z")
                timenow = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
                delta = timenow - reporttime
                print("{} second(s) before.".format(delta.seconds))
                if delta.seconds < 120:
                    flag = True

            # data = login.session.get('https://weixine.ustc.edu.cn/2020/apply/daliy/i', headers=headers).text
            # data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
            # soup = BeautifulSoup(data, 'html.parser')
            # token = soup.find("input", {"name": "_token"})['value']

            data = login.session.get('https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3', headers=headers).text
            data = data.encode('ascii', 'ignore').decode('utf-8', 'ignore')
            soup = BeautifulSoup(data, 'html.parser')
            start_date = soup.find("input", {"id": "start_date"})['value']
            end_date = soup.find("input", {"id": "end_date"})['value']
            data = {
                '_token': token,
                'start_date': start_date,
                'end_date': end_date,
                'return_college[]': '东校区',
                'return_college[]': '西校区',
                'return_college[]': '南校区',
                'return_college[]': '北校区',
                'return_college[]': '中校区',
                't': '3'}
            post = login.session.post('https://weixine.ustc.edu.cn/2020/apply/daliy/post', data=data)
            if post.url != 'https://weixine.ustc.edu.cn/2020/apply_total?t=d':
                flag = False

            if flag:
                print("Report SUCCESSFUL!")
            else:
                print("Report FAILED!")
            return flag
        else:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='URC nCov auto report script.')
    parser.add_argument('username', help='your student number', type=str)
    parser.add_argument('password', help='your CAS password', type=str)
    parser.add_argument(
        '--data_path', help='path to your own data used for post method', type=str, default='data.json')
    parser.add_argument(
        '--cont_name', help='your contact\'s name', type=str)
    parser.add_argument(
        '--cont_rel', help='your contact\'s relationship with you', type=str)
    parser.add_argument(
        '--cont_num', help='your contact\'s number', type=str)
    args = parser.parse_args()
    autoreporter = Report(username=args.username, password=args.password, data_path=args.data_path,
                          cont_name=args.cont_name, cont_rel=args.cont_rel, cont_num=args.cont_num)
    count = 1
    while count != 11:
        ret = autoreporter.report()
        if ret:
            break
        print("*\n* Run " + count + " Failed, retry...\n*")
        count = count + 1
    if count != 11:
        exit(0)
    else:
        exit(-1)
