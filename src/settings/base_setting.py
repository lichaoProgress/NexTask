#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 项目服务配置模块 }
import logging

server_host = "0.0.0.0"
server_port = 8099
server_log_level = logging.WARNING
server_access_log = True

allow_origins = [
    # "*",
    "http://127.0.0.1",
    "http://localhost",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:6969",
    "http://localhost:6969",
    "http://43.138.173.93:6969",
]
frontend_index_url = "http://127.0.0.1:5173/" # local dev
# frontend_index_url = "http://127.0.0.1:6969/"   # local docker
# frontend_index_url = "http://43.138.173.93:6969/"  # product nginx
