# 中国滑稽大学(University of Ridiculous of China)健康打卡平台自动打卡脚本

## Current README

Fork & rework of https://github.com/Kobe972/USTC-ncov-AutoReport.

**Daily Report & Cross-campus Report supported; should work as of April 3, 2022.**

usage: report.py [-h] [--data_path DATAPATH] [--max_tries MAXTRIES] username password

Updates:
- Fixed Daily Report & Cross-campus Report in light of March 2022 changes by URC.
- Added try-catch logic, error logging and max_tries argument (default 10) as robustness measures.
- Personal information (dorm, contact) is now primarily loaded from the previous report.
- Now scheduled twice a day at 23:58 and 11:58 UTC+8; also able to run manually (see action page)

## Past README (Obsolete)

usage: report.py [-h] [--data_path DATAPATH] [--cont_name CONTNAME] [--cont_rel CONTREL] [--cont_num CONTNUM] username password

See https://github.com/xbb1973/USTC-ncov-AutoReport and https://github.com/Kobe972/USTC-ncov-AutoReport for GitHub Actions configure; note, however, that Secrets change to the format as follows.

|GitHub Actions Secrets|Arguments|Value|Default|
|:-:|:-:|:-:|:-:|
|USERNAME|username|your student number|(required)|
|PASSWORD|password|your CAS password|(required)|
|/|--data_path|path to your own data used for post method|data.json|
|CONTNAME|--cont_name|your contact's name|张三|
|CONTREL|--cont_rel|your contact's relationship with you|无|
|CONTNUM|--cont_num|your contact's number|13800138000|
