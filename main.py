#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 主入口模块 }

import uvicorn
from py_tools.logging import logger

from src import settings
from src.server import app


def main():
    logger.info(f"project run {settings.server_host}:{settings.server_port}")
    uvicorn.run(
        app=app, host=settings.server_host, port=settings.server_port, log_level=settings.server_log_level, access_log=False
    )


if __name__ == "__main__":
    main()
