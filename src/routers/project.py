#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 模块描述 }
from src.controllers.project import ProjectController, ProjectDetailControllers
from src.data_models.api_models import base_api, project_api
from src.data_models.api_models.base import SuccessRespModel
from src.routers.base import BaseAPIRouter

router = BaseAPIRouter()

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.create_project,
    response_model=base_api.PKRespModel,
    methods=["POST"],
    summary="任务创建",
)

router.add_api_route(
    path="/v1/projects/{project_id}",
    endpoint=ProjectController.update_project,
    response_model=SuccessRespModel,
    methods=["PUT"],
    summary="任务更新",
)

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.query_projects,
    response_model=project_api.ProjectListOut,
    methods=["GET"],
    summary="任务分页查询",
)

router.add_api_route(
    path="/v1/projects",
    endpoint=ProjectController.delete_project,
    response_model=SuccessRespModel,
    methods=["DELETE"],
    summary="任务删除",
)

router.add_api_route(
    path="/v1/projects/detail",
    endpoint=ProjectDetailControllers.detail_project,
    response_model=project_api.ProjectDetailOut,
    methods=["GET"],
    summary="任务详情",
)
