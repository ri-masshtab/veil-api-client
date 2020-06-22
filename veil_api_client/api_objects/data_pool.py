# -*- coding: utf-8 -*-
"""Veil data-pool entity."""
from ..base.api_object import VeilApiObject


class VeilDataPool(VeilApiObject):
    __API_OBJECT_PREFIX = 'data-pools/'

    def __init__(self, client, datapool_id: str = None):
        super().__init__(client, api_object_id=datapool_id, api_object_prefix=self.__API_OBJECT_PREFIX)
        self.description = None
        self.type = None
        self.used_space = None
        self.shared_storage = None
        self.size = None
        self.free_space = None
        self.created = None
        self.path = None
