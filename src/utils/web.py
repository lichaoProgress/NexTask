#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 模块描述 }
from py_tools.enums.error import BaseErrCode

from src.enums import BizErrCodeEnum


def success_api_resp(data=None):
    """成功的响应"""
    data = data or {}
    resp_content = {"code": BizErrCodeEnum.OK.value, "message": BizErrCodeEnum.OK.desc, "data": data or {}}
    return resp_content


def fail_api_resp_with_err_enum(err_enum: BaseErrCode, err_msg: str = None, data=None):
    """失败的响应携带错误码"""
    resp_content = {
        "code": err_enum.code,
        "message": err_msg or err_enum.msg,
        "data": data or {},
    }
    return resp_content


def fail_api_resp(err_msg: str = None, data=None):
    """失败的响应 默认Failed错误码"""
    resp_content = {
        "code": BizErrCodeEnum.FAILED.code,
        "message": err_msg or BizErrCodeEnum.FAILED.msg,
        "data": data or {},
    }
    return resp_content
