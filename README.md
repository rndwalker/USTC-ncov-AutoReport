## URC (University of Ridiculous of China) nCov Auto Report

> Disobedience is the true foundation of liberty.
> &mdash; <cite>Henry David Thoreau</cite>

> Freedom is something people take, and people are as free as they want to be.
> &mdash; <cite>James Baldwin</cite>

## Current README

Fork & grand rework of https://github.com/Kobe972/USTC-ncov-AutoReport.

**Screenshot (with fake QR code) auto generation WIP; when finished, should work as of May 3, 2022.**

### Usage

```
py report.py [-h] [-p DATA_PATH] [-t MAX_TRIES] [-n REAL_NAME] [-m MOBILE_PHONE]
```

|Abbreviation|Arguments|Help|Default|
|:-:|:-:|:-:|:-:|:-:|
|(positional)|username|your student number|(required)|
|(positional)|password|your CAS password|(required)|
|-dsc|(none)|runs Daily Report/Screenshot Generation/Cross-campus Report|(none)|
|-p|DATA_PATH|path to your own data.json|'data.json'|
|-t|MAX_TRIES|max tries as in reports|5|
|-n|REAL_NAME|your real name to generate screenshots|(when empty, read from previous report)|
|-m|MOBILE_PHONE|your mobile phone to generate screenshots|(when empty, read from previous report)|

**Expected Output:**

```
Login Successful!
Got Daily Report Success Alert!
Last report: %H hour(s) %M minute(s) %S second(s) before.
Daily Report Successful!
Cross-campus Report Successful! Until: %Y-%m-%d %H:%M:%S
```

### GitHub Actions

- Fork, or make a new repository with downloaded source code;
- Settings > Secrets > Actions > New Secret > `USERNAME` & `PASSWORD` as student number and password;
- For screenshot generation, `REAL_NAME` & `MOBILE_PHONE` as real name and mobile phone (formed `189****0604`) as well;
- Actions > `I understand my workflows, go ahead and enable them` > Auto-report action > `Run workflow` for test.

See https://github.com/Kobe972/USTC-ncov-AutoReport for further instructions.

### Updates

- **Generates screenshot with fake QR code for now. (WIP)**
- Minor adjustments & performance optimization. Action should now run in ~30s.
- Fixed Cross-campus Report in light of change of April 5, 2022.
- Fixed Daily Report & Cross-campus Report in light of March 2022 changes by URC.
- Added try-catch logic, error logging and max_tries argument (default 10) as robustness measures.
- Personal information (dorm, contact) is now primarily loaded from the previous report.
- Now scheduled daily at **23:55 (~0:05)** UTC+8.
- Has a `workflow_dispatch` event trigger (can be run manually, see Actions after forking).

> Men cannot live free, but he can die free.