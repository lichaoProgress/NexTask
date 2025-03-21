#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 自定义异常包 }
from py_tools.exceptions.base import (
    MaxTimeoutException,
    SendMsgException,
    MaxRetryException,
    BizException,
    CommonException,
)

__all__ = ["MaxTimeoutException", "SendMsgException", "MaxRetryException", "BizException", "CommonException"]
