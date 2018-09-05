#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 4:31 PM
# @Author  : vell
# @Email   : vellhe@tencent.com
import json

from tornado.web import RequestHandler


class BaseReqHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.json_args = None

    def data_received(self, chunk):
        pass

    def prepare(self):
        if 'Content-Type' in self.request.headers and self.request.headers['Content-Type'].startswith(
                'application/json') \
                and self.request.body:
            # print(self.request.body)
            self.json_args = json.loads(self.request.body.decode())
        else:
            pass
        super().prepare()
