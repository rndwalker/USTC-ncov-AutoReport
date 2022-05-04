headers = {
	# noinspection SpellCheckingInspection
	'authority': 'weixine.ustc.edu.cn',
	'origin': 'https://weixine.ustc.edu.cn',
	'upgrade-insecure-requests': '1',
	'content-type': 'application/x-www-form-urlencoded',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
	              'Chrome/99.0.4844.51 Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
	          'q=0.8,application/signed-exchange;v=b3;q=0.9',
	'referer': 'https://weixine.ustc.edu.cn/2020/',
	'accept-language': 'zh-CN,zh;q=0.9',
	'Connection': 'close',
}
cross_data = {"return_college[]": [
	"中校区",
	"西校区",
	"南校区",
	"北校区",
	"东校区"
], "reason": "实验、自习", "t": "3"}

home_url = 'https://weixine.ustc.edu.cn/2020'
daily_url = 'https://weixine.ustc.edu.cn/2020/daliy_report'
cross_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3'
cross_return_url = 'https://weixine.ustc.edu.cn/2020/apply_total?t=d'
cross_post_url = 'https://weixine.ustc.edu.cn/2020/apply/daliy/post'

# noinspection SpellCheckingInspection
logo_base64 = 'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACXBIWXMAAAsTAAALEwEAmpwYAAAGzmlUWHRYTUw6Y29tLmFkb2Jl' \
              'LnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4' \
              'bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDggNzkuMTY0MDM2LCAyMDE5LzA4' \
              'LzEzLTAxOjA2OjU3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRm' \
              'LXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20v' \
              'eGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDov' \
              'L25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20v' \
              'eGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIiB4' \
              'bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5jb20vcGhvdG9zaG9wLzEuMC8iIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUg' \
              'UGhvdG9zaG9wIENDIDIwMTkgKFdpbmRvd3MpIiB4bXA6Q3JlYXRlRGF0ZT0iMjAyMS0wNS0xMFQxNTo1MTowMiswODowMCIgeG1w' \
              'Ok1vZGlmeURhdGU9IjIwMjEtMDUtMTBUMTU6NTM6NTkrMDg6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjEtMDUtMTBUMTU6NTM6' \
              'NTkrMDg6MDAiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ODQyZjgxYWItMzE0My00YmNmLTlkYzEtNjkwYTY2NWU0NjE5IiB4' \
              'bXBNTTpEb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6Y2VjODEwMWQtZDgyMC1iMDQzLTkwMmUtNDY4M2ZmODEyN2Ez' \
              'IiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6N0ZCMDcyNUNBNUZFMTFFQUE1RDBBQjY2MTIwRTU4N0IiIGRjOmZv' \
              'cm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiBwaG90b3Nob3A6SUNDUHJvZmlsZT0ic1JHQiBJRUM2MTk2' \
              'Ni0yLjEiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo3RkIwNzI1OUE1RkUxMUVBQTVEMEFC' \
              'NjYxMjBFNTg3QiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo3RkIwNzI1QUE1RkUxMUVBQTVEMEFCNjYxMjBFNTg3QiIvPiA8' \
              'eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1w' \
              'LmlpZDplYTVkNjQ1NS0wZTcwLTRhNTAtYjU1ZS1iNzI0MDU2ZWQwYmYiIHN0RXZ0OndoZW49IjIwMjEtMDUtMTBUMTU6NTM6NTkr' \
              'MDg6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMS4wIChNYWNpbnRvc2gpIiBzdEV2dDpjaGFuZ2Vk' \
              'PSIvIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo4NDJmODFhYi0zMTQz' \
              'LTRiY2YtOWRjMS02OTBhNjY1ZTQ2MTkiIHN0RXZ0OndoZW49IjIwMjEtMDUtMTBUMTU6NTM6NTkrMDg6MDAiIHN0RXZ0OnNvZnR3' \
              'YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMS4wIChNYWNpbnRvc2gpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDwvcmRmOlNlcT4g' \
              'PC94bXBNTTpIaXN0b3J5PiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0i' \
              'ciI/Pq9s1TgAABESSURBVHic7Z15dCTFfcc/Pfdo7kOalVZa7Up7H4LsLizmcsAGBzvmjiEmIc9xjP3iJc/xH2sHXvxHHD9jjoTg' \
              'h1+MIQQMmCO24wtizANzL+yBl0V737u6NaNjZjRXT3f+GEmWdrpnumd6Rrugz19Sd9WvSv1VdVX96lfVgizLKOAGvg1cBywELEqJ' \
              '5tGFDOSAPuBnwLeAxOmJBAVB7gK+DlhrXMGPOjngfmDLzIszBbEBrwGb6lqted4BLgWyMFuQrcyLMVe8A1wAYJq8cC/zYswlmyho' \
              'gCDLshsYBcxzWaN5yAN+E3A382KcCZiBewRZlk8CrXNdm3kA6BFkWc4xP884UxAFWWVmOM/cUKeWIZNN9CCmo+Sz4+RzcaRcAjmf' \
              'rU/xejBZMds8mK0eLHYvZnsQm7sVEOpSfO0EkfNMRN8nObCN5OB2xMxYzYqqNWabF1fTRtyR82kId4FQuzFQTV5Zib43iR58mtzE' \
              'oNGm5xyrM0xw2c14Wi6piX1DBUnF9hDd/2PSY0eMMnnGYvcuIbzyr3EG1xhq1zBBRg7/lNih5/iojRGCS28guPRzhtmrWhBZyjG4' \
              '+wfE+94yqk5nHe4FFxDp+iqCyVa1raoEkfNperZ9m/Tooaorcrbj8HWw8PxvIZidVdkxlU+izsD7358XY5L02BH6//AAhXWoyqlY' \
              'kNjBZ0gMbK+q8A8byaGdRA/8pCobFQmSHNxG7PDPqirYCASzHbM9gM3dis3TjsnqmesqMXLkFyT6t1acX//EUBYZ3vd4xQVWgmC2' \
              '4/AvxxlYhTO4Cpu7DZOlAcFUPEGT8lnE9DBiOkpuYpD0yD5SsW7EdLRu9R3e9ziupg0IJv2r4Lo79bHjzzO09zHdBelFMDvxtl6G' \
              'p/ki7N4lig9fD5n4CeK9b5Doe6Mu4oRX3IJ/ydW68+kSRBJTHH/tdvLZuO6CtGJxNuFvvwpv62WYLNWNWJSQZYnkwLuMHP0lmbHD' \
              'htufwmx10/7xBzBZXLry6RKklq3D4mwkvPJWXE0bEYSqBn+aSQ7tZHjf4+SSfTWxX0kr0dWHJAbe1WVcK962KwmvuAWTxVET+2q4' \
              'GtfTEOpi9NhviB58BuS8ofaTg9tqJ4iUi5Me2a+7UiULdzbStPYrNITWGmpXD4LJQqDjGhyBlfT/4d/JZ0YMs50ePUg+O4bZ5kNG' \
              'RtDgwtf8bkgO7kSWpaoqOBNXZBOLLrp3TsWYiTOwgkUX3Y0ztM4wm7IskxzcoSuPZkHSo8a1Dk/LJSw492t1f0WVw2zz0rLxDgKd' \
              '1xtmMz2yr/CDxq5a8ytLTMcqqtDpeFsvp3HNl+rWcetFEEyElt2EIFiIHXq2anuizleg5qei17ASvkVX0rjmtjNWjJkEl96Ab9GV' \
              'VdvR2ydpfjLVdnbu5otpXP1FBKE+a9NGEF71BdwLLqjKhpiulSDZcd2VmcLijNC05u8qzj9XCIKJSNftOIOrK7aRzyXQ4wHW3IdU' \
              'vGwimFlw7j9UPesWM6MFn1RquPDPIZhwNW3AGVg5K10mfpyJoV3kUgMAWJ0RGsJd2L2LK6u+yULTuq9y4o2vI+czlVVex7OreRhQ' \
              'aNlNOHxLK86fiu0hevCZP45WALPNR9Pa22aJkU2cYrD7YdIje4tsRA88iTO4lqa1X8ba0KS7DlZnmNCym+riVK2pIM7g6oocbACy' \
              'JDLY/TDxnldmXbd7l9C8/htYHIHpa6nYHnp3fA85n1a1l4p9wMm3vknLxm/i8C/XXR9f+1XEe18nM35Ud1491HS4E1x2c0WdeD6b' \
              'oGfbvxaJYXW10LLxjlliZJN99O28p6QYU0hikp5t3yEVK25F5RAEE01rv0ytA+ZqJogzuBpnYIXufNlkL6e23ln06rE4QrRsvBOz' \
              'zTt9TRJT9O28B0mc0Gxfzqfp3fFdJqIf6K6b3bsEd/PHdOfTQ80ECXRcpztPNtnHqa3/TG6if/YNwUzz+i1YneHpS7IsM/D+g+SS' \
              'PUV2nKF1NK75kmowm5zP0LfzHjLxk7rr6Fv0Kd159FATQey+zkLIpQ7yuQR9O76HlCvamEqw84aiUdL4yZdIDm4rSutpuZSWjXfi' \
              'a/skka7NhFf+jWJ5cj5N3857yGeLyyuFM7ASm6ddVx491EQQ/+LP6EovSyL9791HbqJ4XcLu7STQce2sa7nUMMP7nyhKa21opmnt' \
              'bbP6Lf/iT6v6psTUAP277tftNK1lK6mBIAIN4XM0p5ZlmcHuh0jF9iiYMtG07itFy7dD3Q8pduKhFZ9XXMcOLv0czpByi01FdzN6' \
              '9Fea6wvgabkYwVwbx6jhgth9nZitbk1pZSlfiHrseVXxvn/xn2P3LJp1Ld73JhPDu4rSWl0LcTWdp2hHEAQiXZsxqdQrdug5sjpW' \
              'DU1me0UDFk22jTaope8Y3v8UvTvu4tirm4n3vqaYxuJsJLj0xlnXZEkkeuBpxfSBjmtKDrEtdh+h5Z9XvCdLOQY/+KEub4TjNA+B' \
              'UdRAkPKvK9+iK8kmesln1F36Um6Coe6HZ8UMj514ETFVvMXB4gjhab64bLne1suxq3gN0iN7GT/5UlkbU5zusjEKQwURTFYcvmVl' \
              '01mdYeyetpJpJDFJvPc1EpOCSOKEanCef8lnNYUJCYJA4+ovoja5G97/pOZ1H7tvaU027hgqiNnu1/RgUrE9JAc1hKEKJkLL/xKA' \
              'kaO/RsoVhx+ZrC68rZdrrqPD14G37QrFe3I+xWD3jzTZMZlt2Gsw/DVUEIvdXzaNLOUZ2vNfmux5Wy/H5l6IJKYYO/6CcpqFl2Ey' \
              '2/+smnGTrxINqE+Qw503liIzTLbCS79i8k8v1NxjwjTcwJJTDOw+weMn3oFWRJL19PqJrziFtX7Q3sf1bT+Y7ZpG03qwVBvr7lMC' \
              'xEzY8QOPaN63xXZRGhZQYRcagiL3Y8s5Rg99mvF9A2N66fd6fG+N4j3vEq851Vih57Dv+RqfG2fRDAp/4mehX/K6PH/Ixs/VnRPy' \
              'sUZ2vsYC865veTfozaMroa6vrKiB55CElOq92cOc63ORgDGT/2efFZ5B6+//Y8z5rHjv53+WUxHGd77KCffvoNM/LhiXkEQCK9QH' \
              'gYDJPreIDm0U/U+oHm+pYe6RRukRw8S7/m96n1X5PyiSSAUXnFKWBzh6dl3KraXbOJEUZps/Dgn3/onRo78r6KNhvA5OIPqcWFD3' \
              'Y8giepufSO2sJ2OoYLkFRyDUHCPDO15tGTeoIK/KT16SPFBA4Vw/8mJYCrWrW5YzhM98JPJiV+xzypUoi8R08MlQ4HyCqO+ajFWE' \
              'JWo+PFTL5MZV480b2hcj927pOj6WImJmqtpw/TPwaU3El71tyX3Y4yfepn+9+5DlmbH7zp8HbgXqK9xjB57XnWbdz4zqpqvUgwVR' \
              'Ml1ns8ly27zUmodkpgi0a+8s1cwO4r2h/vbP0XbhXeVdI0nB7cXgqpPI7T85hKTPLngzFRoXWp9WzXU/JUVO/iM4oRuCmeoC4e/e' \
              'HafGNimGuXhDK5WHD3Z3K20few7uJsvUi1v9OgvipyT1oYFeFs/oZonM36U0WPPF12vxXEhhgqSS/bNctBl4sdVO+UpgktvULyut' \
              'Pg0hcPXqXpPMFmJdG0uecLCwO7/LHp1BTuvLekKiR16llxqaPp3WZYQJ0ONjMTYV5aYnLXIVOjI1T2ohXX3YiedlM8qutinsJcQB' \
              'MoHJOQzsSLBLY4Q3tbLVG3K+QxD3Y9M/54ZP1JyCF8phg97p/aQxHvfVIyRmkmgU7l1pKIflAxKK9VCprA2REq6yMdO/LboWqDj2' \
              'pKtZGL4vWnvc6qCIAktGC5IcnA7kphmeP+PS6Zz+Jer7g1JDqnvqRDMzlmRJ6WYGS50OqnYniLPrtXZiKfl0pI2h/f+N/lcsqKoF' \
              'S0YLsjE8C6G9z1WNjhbrXUAZMaVZ9cFpLK+Kii848tt6kyPFZ9CEey8DkpE5+ezYwx1PzQrktJIDBdElnKMn3q5ZBq7twNX47mq9' \
              '5VCe6bt5zOMHvtN6TrIMtH9T5KbKN3pijM66SmsDZGyi12J/q3IUq5kmkqZk8MvS7UOMTNWNvAteuApJqK7cTVuwOqKYHGEQZaQ8' \
              'mkyY0cZ73mFrIoPayZqbpFA53XEe1+n2nNLKqHugtg87bNm2cVoewip6G5S0d1V1cVsV17PsLlacEXOI1mjXcelqPtWpmDn9SWDE' \
              'UyWhrrVpVRUfqDCIPFqqasgVtdCXJHSR8ybzDasroU1r4vN015yz4jDvwxHYFXN63E6dRWkXOuYwqey5m0YgonGVV8om2wuWkndB' \
              'LE2LMDdfKGmtL5FV+Bq2libiggWIus24wyW/+9vaPwTbO7S0TFGUzdBAh3Xat59K5gsLDj3H/EvuRpBZwBDKZzBtbRd+F08LerOx' \
              '1n1EAT8Sz5rWPlaqNsoSy3MUw3BZCG84hYCS64h3vc6qdgeUrG9JT3HxTasOAIrcQbX4GraWDYWTAk9ccpGoFkQs9WtuiKohbGTv' \
              'yvMgnVitrnxt1+Fv/0qZFkmmzhZOEMkMzp5bPk4+WwCk9mO2e7DbPNhsfuwudtw+JerBjlopdwktxwmi7Mw89cYYa+5thZHoCpBY' \
              'gefxmzz4mtTX3cohyAI2D2LFNfea8H4qVeIKSxo6cFiV/enKaG5DzHrNKzEUPePGO9RDq4+00j0b2Xwgx9WbaeUg1MJzYLoVVoZm' \
              'cHdD5ZdtJprkoPb6d9V/ZGvoP8fWbMgSkEIlTK05xGiB5819Lgno4gd/jl9O+817DCz6eemcTeyZkGMnheMHP4pPe/+C7nUsKF2K' \
              '0US0/S992/EDj6NkU5FvaNL7a8sZ2PFx1OokR7Zy8k3t8z5ufET0W5Ovn0HyYF3DLVrc7dibYgAaDpNDnTOQ1xNG8mMH9NdsVJIY' \
              'pKBXf/B2IkXCa+8FYevw1D7pchNDDK8/wnDhZjCHdHXOkDnqaRiOsqJ17+GVMNPFXlaLiHQce3kZ4ZqQzbRy/iplxg78WLNFpoEk' \
              '4X2S+7HMhmjrDmf3oOUo/ufYETnrtVKcARW4Wu7AveCTVVP7qDQRyT632b81CuGHleohn/xZwivvFV3Pt2CSGKS46/eTj6X1F1YJ' \
              'QhmO87gahpC63CG1mFztWgSKJ9LkB49RHpkL6mRfYWvOMjl1+KNwGRpYPHHH6joLPqKvh9Sr+PGlRGwOEJYG5omx/jCtEs/n0sip' \
              'obIpYaR88bHTGklvOKvKnZKVvQu8LV/mtTIARL9b1dUaHXIk4ftnxnD5dNxR86vykNcsfs90vX3hg+Dz3bsnkVEujZXZaNiQQSTj' \
              'eb1W3T7aj6sWOx+mtdvqXr9puqPguUzMXp33F3zk9bOZOyedpo3fAOLI1S1LUM+mydLWQbef7CqL8ucrbgj5xHput2wlU1DPyw5d' \
              'vwFYof/R/cZVGcjZqubQOf1uo+iKofhn16VxAlGjvyc0WMv1GwWPJcIJgv+9j8j0HE9Jqu+j7Vosl+rz3eL6Sjx3tdJDrxLuoZfs' \
              'qkXDl8Hrqbz8Cy8tBC6WiPq8j31wgaZ7YVPeGdGENMj5DMxJA0nidYbk9mB2R7AYg9gcQQnz+HaYEiHrQVBLqwS1fTsUxlZ1+nOZ' \
              'ySCoNmFXg0WIAcYvwN+BgKC5hWzjziiCfjwffT87GXABNTelz6PVn4lyLLsBkYB449Hm0cPeSBoAhLAA3NcmXkKGowLM0a97wDnz' \
              '119PtK8C2yCwrB36qIN2AboOyN8nmrZDWwEsjDb/Z4FzgHupTAUnqe25ID7KDSA6agRQWWi7gbuBq4GIszRbt0PISIwAPwS2EKh/' \
              '57F/wOIDFyRQ0XNswAAAABJRU5ErkJggg=='
