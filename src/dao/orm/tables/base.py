#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @File: base.py
# @Desc: { 模块描述 }
from py_tools.connections.db.mysql import BaseOrmTableWithTS


class BaseTable(BaseOrmTableWithTS):
    """不直接继承第三方库的基类，用于扩展"""

    __abstract__ = True
