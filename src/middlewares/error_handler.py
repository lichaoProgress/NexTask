#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 项目统一错误处理模块 }
from http import HTTPStatus

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from py_tools.exceptions import BizException
from py_tools.logging import logger

from src.enums import BizErrCodeEnum
from src.utils import web


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """全局捕捉参数验证异常"""

    # 格式化参数校验错误信息
    errors = exc.errors()
    formatted_errors = [
        {"field": ".".join(str(loc) for loc in error["loc"]), "message": error["msg"]} for error in errors
    ]
    error_tip = f"参数校验错误 {formatted_errors}"
    logger.error(error_tip)

    error_detail = {"error_detail": formatted_errors}

    return JSONResponse(
        status_code=HTTPStatus.OK,  # 200
        content=web.fail_api_resp_with_err_enum(BizErrCodeEnum.PARAM_ERR, "Validation error", error_detail),
    )


async def global_exception_handler(request: Request, exc: Exception):
    """全局系统异常处理器"""

    if isinstance(exc, ConnectionError):
        message = f"网络异常, {exc}"
        err_enum = BizErrCodeEnum.SOCKET_ERR
    else:
        message = f"系统异常, {exc}"
        err_enum = BizErrCodeEnum.SYSTEM_ERR

    logger.exception(f"global_exception_handler {message}")
    return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=web.fail_api_resp_with_err_enum(err_enum))


async def biz_error_handler(request: Request, exc: BizException):
    """业务错误处理"""
    logger.error(f"biz_error_handler {exc} {exc.msg}")
    return JSONResponse(status_code=HTTPStatus.OK, content=web.fail_api_resp(exc.msg))


def register_exception_handler():
    """注册异常处理器"""
    return {
        RequestValidationError: validation_exception_handler,  # 请求参数校验错误处理
        BizException: biz_error_handler,  # 业务错误处理
        Exception: global_exception_handler,  # 全局未捕获的异常处理(默认走中间件处理)
    }
