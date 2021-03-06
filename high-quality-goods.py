from bs4 import BeautifulSoup
import requests
import time
import re
import os

import requests
import json

def ariato():

    ip = "*****:6800"  ##  IP得带端口号
    token = "8118bd19bd81002b482f"  ##  token为RPC密码
    i = 0 ## i为循环数


    posturl = 'http://'+ip+'/jsonrpc'

    with open("mag.txt","r",encoding="utf-8") as file:
        all = file.readlines()

    Header = {
        "Host":ip,
        "Proxy-Connection":"keep-alive",
        "Content-Length":"231",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"application/json, text/plain, */*",
        "Origin":"http://"+ip,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Content-Type":"application/json;charset=UTF-8",
        "Referer":"http://"+ip,
        "Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
    }

    for list in all:

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
            print("第"+str(i)+"行传输成功，返回："+str(post)+"\n")

        except:
            print("第"+str(i)+"行传输失败，无返回。"+"\n")

    with open("mag.txt","r+",encoding="utf-8") as file:
        file.truncate(0)



class soup:

    for sentry in range(50,1,-1):
        list = requests.get("*****"+str(sentry))  ##url
        soup = BeautifulSoup(list.content, "lxml")

        body = soup.find('tbody')
        success = body.find_all("tr",attrs={"class":"success"})
        for i in success:
            magnet = i.find_all("a", attrs={"href": re.compile(r"magnet(\s\w+)?")})
            for i in magnet:
                with open("mag.txt", "a", encoding="utf-8") as file:
                    file.write(i["href"] + "\n")
        if sentry % 10 == 0:
            ariato()
            time.sleep(3)
        time.sleep(1)



