#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 16:51
# @Author  : zjk
# @FileName: douyinqushuiyin.py
# @Software: PyCharm

import requests, re
import flask, json
import urllib3

urllib3.disable_warnings()
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
api = flask.Flask(__name__)


@api.route('/api', methods=['get'])
def qushuiyin():
    get_url = flask.request.args.get('url')
    status = 115
    title = ""
    url = ""

    if get_url:
        address = re.findall('v.douyin.com', get_url)
        if address:
            pat = '(https://v.douyin.com/.*?/)'
            url = re.compile(pat).findall(get_url)[0]  # 正则匹配分享链接
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36'
            }
            r = requests.get(url, headers=headers, verify=False)
            try:
                title = re.findall('<title data-react-helmet="true"> (.*?)</title>', r.text, re.S)[0]
                html_data = re.findall('src(.*?)vr%3D%2', r.text)[1]
                url = requests.utils.unquote(html_data).replace('":"', 'http:')
            except:
                msg = "\u5730\u5740\u89e3\u6790\u5931\u8d25\uff01"
                data = {"status": status, "msg": msg, "data": {"title": title, "url": url}}
                return json.dumps(data)
            status = 101
            msg = "\u89e3\u6790\u6210\u529f"
        else:
            msg = "\u8bf7\u8f93\u5165\u6296\u97f3\u590d\u5236\u7684\u94fe\u63a5\uff01"
    else:
        msg = "\u8bf7\u6c42\u53c2\u6570\u9519\u8bef\u6216\u53c2\u6570\u503c\u4e0d\u5b58\u5728\uff01"

    data = {"status": status, "msg": msg, "data": {"title": title, "url": url}}
    return json.dumps(data)


if __name__ == "__main__":
    api.run(port=8888, debug=True, host='127.0.0.1')  # 启动服务
