#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import advHandler


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/api/check/getGG", advHandler.AdvHandler),
        ]
        settings = {'cookie_secret': 'zhaoyf', 'gzip': True}
        tornado.web.Application.__init__(self, handlers, **settings)
