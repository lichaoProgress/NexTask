#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 用户模块 }
from fastapi import Query

from src.data_models.api_models import user
from src.data_models.api_models.base import SuccessRespModel


class UserDetailControllers:
    """用户详情信息路由处理"""

    @classmethod
    async def detail(cls):
        return SuccessRespModel()
