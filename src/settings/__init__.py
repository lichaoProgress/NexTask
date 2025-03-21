#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 项目配置包初始化 }
from src.settings.base_setting import (
    server_host,
    server_log_level,
    server_port,
    server_access_log,
    allow_origins,
    frontend_index_url,
)
from src.settings.db_setting import (
    mysql_dbname,
    mysql_host,
    mysql_password,
    mysql_port,
    mysql_user,
    sql_echo,
    redis_db,
    redis_host,
    redis_password,
    redis_port,
)
from src.settings.log_setting import console_log_level, logging_dir, log_format
from src.settings.auth_setting import auth_whitelist_urls
