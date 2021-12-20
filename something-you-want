from bs4 import BeautifulSoup
import requests
import time
import re
import os

import requests
import json


def ariato(magnet):
    i = 0  ##跑循环
    ip = "*****:6800"  ##  IP得带端口号
    token = "8118bd19bd81002b482f"  ##  token为RPC密码
    posturl = 'http://' + ip + '/jsonrpc'
    list = magnet

    Header = {
        "Host": ip,
        "Proxy-Connection": "keep-alive",
        "Content-Length": "231",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/plain, */*",
        "Origin": "http://" + ip,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "http://" + ip,
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    try:
        i = i + 1
        payloadData = {
            "jsonrpc": "2.0",
            "method": "aria2.addUri",
            "id": "QXJpYU5nXzE2Mzk5MzMwMjJfMC4xODE0MjY3NzE3MzUyMDAyOA==",
            "params":
                ["token:" + token,
                 [list], {}]
        }
        post = requests.post(posturl, data=json.dumps(payloadData), headers=Header)
        print("第" + str(i) + "行传输成功，返回：" + str(post) + "\n")

    except:
        print("第" + str(i) + "行传输失败，无返回。" + "\n")


class test:
    l = 0
    url = "*****"  ##magnet:?xt=urn:btih:
    list = requests.get(url)
    soup = BeautifulSoup(list.content, "lxml")

    page_place = soup.find("ul", attrs={"class": "pagination"})
    page = page_place.find_all("li")
    page_max = int(page[-2].text)

    for sentry in range(page_max,1,-1):
        list = requests.get(url+"&p="+str(sentry))
        soup = BeautifulSoup(list.content, "lxml")
        magnet = soup.find_all("a", attrs={"href": re.compile(r"magnet(\s\w+)?")})
        for i in magnet:
            print(i['href'])
            l = l + 1
    print(l)
