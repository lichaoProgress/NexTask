#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { DAO层初始化模块 }

from py_tools.connections.db.mysql import DBManager, SQLAlchemyManager

from src import settings
from src.dao.orm.tables import BaseTable
from src.dao.redis import RedisManager


async def init_tables():
    # 根据映射初始化库表
    async with DBManager.connection() as conn:
        await conn.run_sync(BaseTable.metadata.create_all)


async def init_orm():
    """初始化mysql的ORM"""
    db_client = SQLAlchemyManager(
        host=settings.mysql_host,
        port=settings.mysql_port,
        user=settings.mysql_user,
        password=settings.mysql_password,
        db_name=settings.mysql_dbname,
    )
    db_client.init_mysql_engine(echo=settings.sql_echo)
    DBManager.init_db_client(db_client)

    await init_tables()
    return db_client


async def init_redis():
    RedisManager.init_redis_client(
        async_client=True,
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
        db=settings.redis_db,
    )
