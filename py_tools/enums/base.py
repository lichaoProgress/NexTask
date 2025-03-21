#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: LC
# @Desc: { 模块描述 }
from enum import Enum


class BaseEnum(Enum):
    """枚举基类"""

    def __new__(cls, value, desc=None):
        """
        构造枚举成员实例
        Args:
            value: 枚举成员的值
            desc: 枚举成员的描述信息，默认None
        """
        if issubclass(cls, int):
            obj = int.__new__(cls, value)
        elif issubclass(cls, str):
            obj = str.__new__(cls, value)
        else:
            obj = object.__new__(cls)
        obj._value_ = value
        obj.desc = desc
        return obj

    @classmethod
    def get_members(cls, exclude_enums: list = None, only_value: bool = False, only_desc: bool = False) -> list:
        """
        获取枚举的所有成员
        Args:
            exclude_enums: 排除的枚举类列表
            only_value: 只需要成员的值，默认False
            only_desc: 只需要成员的desc，默认False

        Returns: 枚举成员列表 or 枚举成员值列表

        """
        members = list(cls)
        if exclude_enums:
            # 排除指定枚举
            members = [member for member in members if member not in exclude_enums]

        if only_value:
            # 只需要成员的值
            members = [member.value for member in members]
            return members

        if only_desc:
            # 只需要成员的desc
            members = [member.desc for member in members]
            return members

        return members

    @classmethod
    def get_values(cls, exclude_enums: list = None):
        return cls.get_members(exclude_enums=exclude_enums, only_value=True)

    @classmethod
    def get_names(cls):
        return list(cls._member_names_)

    @classmethod
    def get_desc(cls, exclude_enums: list = None):
        return cls.get_members(exclude_enums=exclude_enums, only_desc=True)

    @classmethod
    def get_member_by_desc(cls, enum_desc, only_value: bool = False):
        members = cls.get_members()
        member_dict = {member.desc: member for member in members}
        member = member_dict.get(enum_desc)
        return member.value if only_value else member


class StrEnum(str, BaseEnum):
    """字符串枚举"""

    pass


class IntEnum(int, BaseEnum):
    """整型枚举"""

    pass
