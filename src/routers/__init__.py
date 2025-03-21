#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 模块描述 }
from src.routers import project, user
from src.routers.base import BaseAPIRouter

api_router = BaseAPIRouter(prefix="/api")

api_router.include_router(user.router, tags=["用户模块"])
api_router.include_router(project.router, tags=["任务模块"])
