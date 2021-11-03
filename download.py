# -*- coding: utf-8 -*-
# @Time    : 2021/10/30
# @Author  : lcvy
# @File    : download.py
# @Software: PyCharm
# @Python3.8
import requests
import json

def Download():

    ip = "***:6800"  ##  IP得带端口号
    token = "***"  ##  token为RPC密码
    id = ***  ##  此id号为keep-alive的包特有的
    i = 0 ## i为循环数

    ##list = '***'

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
                "id": id,
                "params":
                    ["token:" + token,
                     [list], {}]
            }
            post = requests.post(posturl, data=json.dumps(payloadData), headers=Header)
            print("第"+str(i)+"行传输成功，返回："+str(post)+"\n")

        except:
            print("第"+str(i)+"行传输失败，无返回。"+"\n")
