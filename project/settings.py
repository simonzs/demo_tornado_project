#coding: utf-8

import os
import tornado.options
from tornado.options import define, options

define('port', type=int, default=8000, help='run server on the given port')

settings = {
    'path': os.path.dirname(__file__),
    'status_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'cookie_secret':'2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=',
    'xsrf_cookies': 'nbiD8f1oSuOnAYogv4t4vhaiUFno0k1xpigHKYD3VTY=',
    'debug':True,
}

import uuid, base64
cookie_secret = base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)

class APISettings():

    def __init__(self):
        tornado.options.parse_command_line()


_setttings = APISettings()
