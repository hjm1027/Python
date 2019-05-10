import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = 'http://ssfw.xmu.edu.cn/cmstar/index.portal'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'JSESSIONID=xxxxxxxxxxxxxxxxxxxxxx; iPlanetDirectoryPro=xxxxxxxxxxxxxxxxxx'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
