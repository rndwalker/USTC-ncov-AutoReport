# 中国滑稽大学(University of Ridiculous of China)健康打卡平台自动打卡脚本

## Current README

Fork & grand rework of https://github.com/Kobe972/USTC-ncov-AutoReport.

**Daily Report & Cross-campus Report supported; should work as of April 8, 2022.**

usage: report.py [-h] [--data_path DATAPATH] [--max_tries MAXTRIES] username password

### Updates
- **Fixed Cross-campus Report in light of April 5, 2022 change.**
- Fixed Daily Report & Cross-campus Report in light of March 2022 changes by URC.
- Added try-catch logic, error logging and max_tries argument (default 10) as robustness measures.
- Personal information (dorm, contact) is now primarily loaded from the previous report.
- Now scheduled twice a day at 23:58 and 11:58 UTC+8; also has a `workflow_dispatch` event trigger (can be run manually, see [Actions page](actions/workflows/report.yml) after forking).
