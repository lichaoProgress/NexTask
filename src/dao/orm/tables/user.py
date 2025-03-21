#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 用户数据表模型 }
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.dao.orm.tables import BaseTable


class UserTable(BaseTable):
    """用户表"""

    __tablename__ = "user"
    username: Mapped[str] = mapped_column(String(20), comment="用户昵称")
    password: Mapped[str] = mapped_column(String(20), comment="用户密码")
    phone: Mapped[str] = mapped_column(String(11), default="", comment="手机号")
    email: Mapped[str] = mapped_column(String(20), default="", comment="邮箱")
    github_uid: Mapped[int] = mapped_column(default=0, comment="Github UID")
