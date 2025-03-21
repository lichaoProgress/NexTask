#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 时间数据模型 }
from pydantic import BaseModel


class DateDiff(BaseModel):
    years: int
    months: int
    days: int
    hours: int
    minutes: int
    seconds: int
