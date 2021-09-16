#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 16:07
# @Author  : zhangjiankang
# @FileName: qushuiyin.py
# @Software: PyCharm

import requests, re


class Qushuiyin:
    def geturl(self, share):
        pat = '(https://v.douyin.com/.*?/)'
        url = re.compile(pat).findall(share)[0]  # 正则匹配分享链接
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
        }
        r = requests.get(url, headers=headers)

        title = re.findall('<title data-react-helmet="true"> (.*?)</title>', r.text, re.S)[0]
        html_data = re.findall('src(.*?)vr%3D%2', r.text)[1]
        video_url = requests.utils.unquote(html_data).replace('":"', 'http:')

        data = {"status": 101, "msg": "\u89e3\u6790\u6210\u529f", "data": {
            "title": title,
            "url": video_url, "img": ""}}
        return data


if __name__ == "__main__":
    qushuiyin = Qushuiyin()
    share = input("请输入你要去水印的抖音短视频链接：")
    print(qushuiyin.geturl(share))
