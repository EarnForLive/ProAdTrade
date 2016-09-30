#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web


class AdvHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        return super(AdvHandler, self).get(*args, **kwargs)
