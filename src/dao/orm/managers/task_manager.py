#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @File: task_manager.py
# @Desc: { 模块描述 }
from src.dao.orm.managers.base import BaseManager
from src.dao.orm.tables import TaskTable


class TaskManager(BaseManager):
    orm_table = TaskTable
