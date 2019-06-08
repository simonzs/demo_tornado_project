# coding: utf-8

from project.handlers import (
    base,
)

url_patterns = [
    (r'/', base.BaseHandler),
]
