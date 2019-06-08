# coding:utf-8

import logging
import tornado.web
from tornado.options import options

from project.urls import url_patterns
from project.settings import settings


class TornadoApplication(tornado.web.Application):
    
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoApplication()
    app.listen(options.port)

    #http_server = tornado.httpserver.HTTPServer(app)
    #http_server.listen(options.port)

    #http_server.bind(options.port)
    #http_server.start(0)
    logging.info('start service at: {}'.format(options.port))
    try:
        tornado.ioloop.IOLoop.current().start()
    finally:
        logging.info('stop service')
