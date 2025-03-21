#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { http相关枚举 }

from py_tools.enums.base import BaseEnum


class HttpMethod(BaseEnum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
