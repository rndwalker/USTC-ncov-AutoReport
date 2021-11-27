# 中国滑稽大学(University of Ridiculous of China)健康打卡平台自动打卡脚本

Forked from https://github.com/Kobe972/USTC-ncov-AutoReport

usage: report.py [-h] [--data_path DATAPATH] [--cont_name CONTNAME] [--cont_rel CONTREL] [--cont_num CONTNUM] username password

See https://github.com/xbb1973/USTC-ncov-AutoReport and https://github.com/Kobe972/USTC-ncov-AutoReport for GitHub Actions configure; note, however, that Secrets change to the format as follows.

|GitHub Actions Secrets|Arguments|Value|Default|
|:-:|:-:|:-:|:-:|
|USERNAME|username|your student number|(required)|
|PASSWORD|password|your CAS password|(required)|
|/|--data_path|path to your own data used for post method|data.json|
|CONTNAME|--cont_name|your contact's name|张三|
|CONTREL|--cont_name|your contact's relationship with you|无|
|CONTNAME|--cont_name|your contact's number|13800138000|