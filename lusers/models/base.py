# -*- coding: utf-8 -*-

from lusers import db
from lutils.sqlalchemy import BaseModelMixIn, BaseQuery


class CleanBaseModel(db.Model, BaseModelMixIn):

    __abstract__ = True

    query_class = BaseQuery


class BaseModel(db.Model, BaseModelMixIn):
    __abstract__ = True

    query_class = BaseQuery

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
