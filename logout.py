#!/usr/bin/env python3
# coding: utf-8

import requests
 
data = {
    'action' : 'logout'
	}

headers = {
    'Host': 'net.tsinghua.edu.cn',
	'Origin': 'http://net.tsinghua.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Referer': 'http://net.tsinghua.edu.cn/wired/succeed.html',
	}
 
response = requests.post('http://net.tsinghua.edu.cn/do_login.php', data=data, headers=headers)
print(response.text)
