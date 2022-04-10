## 中国滑稽大学(University of Ridiculous of China)健康打卡平台自动打卡脚本

## Current README

Fork & grand rework of https://github.com/Kobe972/USTC-ncov-AutoReport.

**Daily Report & Cross-campus Report supported; should work as of April 10, 2022.**

### Usage

```
report.py [-h] [--data_path DATAPATH] [--max_tries MAXTRIES] username password
```

Expected Output:
```
Login Successful!
Got Daily Report Success Alert!
Last report: HH小时MM分钟SS秒 before.
Daily Report Successful!
Cross-campus Report Successful! Until: yyyy-mm-dd HH:MM:SS
```

### GitHub Actions

- Fork, or make a new repository with downloaded source code;

- Settings > Secrets > Actions > New Secret > `USERNAME` & `PASSWORD` as student number and password;

- Actions > `I understand my workflows, go ahead and enable them` > Auto-report action > `Run workflow` for test.

See https://github.com/Kobe972/USTC-ncov-AutoReport for further instructions.

### Updates
- Minor adjustments.
- **Fixed Cross-campus Report in light of change of April 5, 2022.**
- Fixed Daily Report & Cross-campus Report in light of March 2022 changes by URC.
- Added try-catch logic, error logging and max_tries argument (default 10) as robustness measures.
- Personal information (dorm, contact) is now primarily loaded from the previous report.
- Now scheduled twice a day at **23:50 (~0:05)** and **22:00 (~22:10)** UTC+8.
- Has a `workflow_dispatch` event trigger (can be run manually, see Actions after forking).
