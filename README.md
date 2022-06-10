## URC (University of Ridiculous of China) nCov Auto Report

> Disobedience is the true foundation of liberty.
> 
> &mdash; <cite>Henry David Thoreau</cite>

> Freedom is something people take, and people are as free as they want to be.
> 
> &mdash; <cite>James Baldwin</cite>

## Current README

Fork & grand rework of https://github.com/Kobe972/USTC-ncov-AutoReport.

**Screenshot (fake) auto generation finished, should work as of May 12, 2022.**

### Usage

```
usage: report.py [-h] [-d] [-s] [-c] [-t MAX_TRIES]
                 [-n REAL_NAME] [-m MOBILE_PHONE] [-i NA_ID]
                 username password
```

| Abbreviation |  Arguments   |                Help                 |   Default   |
|:------------:|:------------:|:-----------------------------------:|:-----------:|
| (positional) |   username   |         your student number         | (required)  |
| (positional) |   password   |          your CAS password          | (required)  |
|     -dsc     |    (none)    |      script running method (*)      |   (none)    |
|      -t      |  MAX_TRIES   |       max tries as in reports       |      5      |
|      -n      |  REAL_NAME   |  your real name as in screenshots   |    (**)     |
|      -m      | MOBILE_PHONE | your mobile phone as in screenshots |    (**)     |

(*) -d Daily Report; -s Screenshot Generation; -c Cross-campus Report

(**) when empty, read from previous report

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
- For screenshot generation, `REAL_NAME` & `MOBILE_PHONE` as real name and mobile phone (as `198****0817`) as well;
- Actions > `I understand my workflows, go ahead and enable them` > Auto-report action > `Run workflow` for test.

See https://github.com/Kobe972/USTC-ncov-AutoReport for further instructions.

## Updates

- **Generates fake screenshots (akm, xck, na test) for now.**
- **Integrates login module for now.**
- **Catches Cross-Campus Report Error for now.**
- Minor adjustments & performance optimization. Action should now run in ~30s.
- Fixed Cross-campus Report in light of change of April 5, 2022.
- Fixed Daily Report & Cross-campus Report in light of March 2022 changes by URC.
- Added try-catch logic, error logging and max_tries argument (default 10) as robustness measures.
- Personal information (dorm, contact) is now primarily loaded from the previous report.
- Now scheduled daily at **23:55 (~0:05)** UTC+8.
- Has a `workflow_dispatch` event trigger (can be run manually, see Actions after forking).

> Man cannot live free, but he can die free.