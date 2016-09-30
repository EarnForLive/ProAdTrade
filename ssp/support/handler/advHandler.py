#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
filename: advHandler.py
author: zhaoyf
"""

import tornado.web


class AdvHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(AdvHandler, self).__init__(application, request, **kwargs)

        # 初始化成员属性
        self.callback = ""
        self.pub = ""
        self.host = '.gdtarget.com'
        self.uid = ""
        self.url = self.host
        self.platform = ""
        self.adtype = ""
        self.league = ""
        self.prp = ""
        self.vtype = 0
        self.location = 0

    def initialize(self):
        pass

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        # 获取callback
        self.callback = self.get_argument("callback", "")
        self.pub = self.get_argument("pub", "")
        self.host = self.get_argument("host", ".gdtarget.com")

        if not self.callback or not self.pub:
            self.finish("")
            return
        self.uid = self.get_secure_cookie("uid")
        if not self.uid:
            self.uid = self.get_argument("uid", "")
            self.set_secure_cookie("uid", self.uid, 36500)

        self.url = self.host
        self.platform = self.get_argument("platform", "")
        self.adtype = self.get_argument("type", "")
        self.league = self.get_argument("league", "")
        self.prp = self.get_argument("prp", "")
        if len(self.adtype) == 6:
            self.vtype = int(self.adtype[2:4])
            self.location = int(self.adtype[-2:0])

        # 判断是否是测试
        test_flag = self.get_argument("test", "0")
        if test_flag.isdigit() and int(test_flag) == 1:
            self.proc_empty_test()
            return

    def proc_empty_test(self):
        pass


