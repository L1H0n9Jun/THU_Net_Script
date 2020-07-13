#!/usr/bin/env python3
# coding: utf-8

import os, sys, time, chardet
import subprocess
import requests
import hashlib


def is_net_ok():
    p = subprocess.Popen("ping -c 2 baidu.com", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    encoding = chardet.detect(stdoutput)['encoding']
    output = stdoutput.decode(encoding)
    retcode = p.returncode
    res = ("ttl=" not in output)

    if res:
        # print('Ping failed.')
        return False
    else:
        # print('Ping success.')
        return True

def login(username, password):
    data = {
        'action': 'login',
        'username': username,
        'password': '{MD5_HEX}' + hashlib.md5(password.encode()).hexdigest(),
        'ac_id': '1'
    }

    headers = {
        'Host': 'net.tsinghua.edu.cn',
        'Origin': 'http://net.tsinghua.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://net.tsinghua.edu.cn/wired/',
    }
 
    try:
        response = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data, headers=headers, timeout=10)
        print(response.text)
    except:
        print("Unfortunitely -- An error happended on requests.post()")


if __name__ == '__main__':
    
    if len(sys.argv) != 3:
       print("Usage: python3 ./keep_connection.py <username> <password>\n")
       os._exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    while True:
        if not is_net_ok():
            print("\n")
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print('The network is disconnected.')
            
            login(username, password)

        else:
            print("\n")
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print('The network is connected.')
            
            time.sleep(900)
