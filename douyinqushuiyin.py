#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 16:51
# @Author  : zjk
# @FileName: douyinqushuiyin.py
# @Software: PyCharm

import requests, re
import flask, json
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
import urllib3

urllib3.disable_warnings()
api = flask.Flask(__name__)


@api.route('/api', methods=['get'])
def qushuiyin():
    q_url = flask.request.args.get('url')
    data = {"status": 115, "msg": "\u89e3\u6790\u51fa\u73b0\u9519\u8bef\uff01", "data": {"title": "", "url": "", "img": ""}}
    if q_url:
        pat = '(https://v.douyin.com/.*?/)'
        url = re.compile(pat).findall(q_url)[0]  # 正则匹配分享链接
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
        }
        r = requests.get(url, headers=headers, verify=False)

        title = re.findall('<title data-react-helmet="true"> (.*?)</title>', r.text, re.S)[0]
        html_data = re.findall('src(.*?)vr%3D%2', r.text)[1]
        video_url = requests.utils.unquote(html_data).replace('":"', 'http:')

        data = {"status": 101, "msg": "\u89e3\u6790\u6210\u529f", "data": {
            "title": title,
            "url": video_url, "img": ""}}
    return json.dumps(data)


if __name__ == "__main__":
    api.run(port=8888, debug=True, host='127.0.0.1')  # 启动服务)
