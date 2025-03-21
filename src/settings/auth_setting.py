#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @File: auth_setting.py
# @Desc: { 模块描述 }
import datetime

# 鉴权白名单路由
auth_whitelist_urls = (
    "/docs",
    "/redoc",
    "/openapi",
    "/api/ping",
    "/api/v1/users/login",
    "/api/v1/users/register",
)

auth_secret_key = "hasjdhaxbxasadjaklkj"
auth_algorithm = "HS256"
auth_expires_delta = datetime.timedelta(hours=6)
