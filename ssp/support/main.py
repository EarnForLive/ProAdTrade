#!/usr/bin/env python
# -*- coding=utf-8 -*-

import handler.application

import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado.options import define, options
define("port", default=8089, help='using the given port', type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(handler.application.Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
