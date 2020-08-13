# -*- coding: utf-8 -*-
"""Veil Task entity."""
from ..base.api_object import VeilApiObject
from ..base.api_response import VeilApiResponse


class VeilTask(VeilApiObject):
    """Veil task entity.

    All requests sent with async=1 will be async task. Here are methods for VeiL
    tasks checking.

    Attributes:
        client: https_client instance.
        task_id: VeiL task id(uuid).
    """

    __API_OBJECT_PREFIX = 'tasks/'

    def __init__(self, client, api_object_id: str = None) -> None:
        """Please see help(VeilTask) for more info."""
        super().__init__(client, api_object_id=api_object_id, api_object_prefix=self.__API_OBJECT_PREFIX)
        self.is_cancellable = None
        self.is_multitask = None
        self.progress = None
        self.error_message = None
        self.executed = None
        self.created = None
        self.name = None
        self.detail_message = None
        self.entities = None

    async def check(self) -> 'VeilApiResponse':
        """Task completion endpoint."""
        url = self.base_url + 'check/'
        response = await self._put(url)
        return response

    async def count(self) -> 'VeilApiResponse':
        """Task counters endpoint."""
        url = self.base_url + 'count/'
        response = await self._get(url)
        return response

    async def cancel(self) -> 'VeilApiResponse':
        """Exit tasks endpoint."""
        url = self.api_object_url + 'cancel/'
        response = await self._put(url)
        return response

    async def jid(self) -> 'VeilApiResponse':
        """Endpoint of receiving jid of a separate task."""
        url = self.api_object_url + 'jid/'
        response = await self._get(url)
        return response

    async def release_locks(self) -> 'VeilApiResponse':
        """Endpoint to reset locks from tasks."""
        url = self.api_object_url + 'release-locks/'
        response = await self._put(url)
        return response

    async def response(self) -> 'VeilApiResponse':
        """Endpoint of receiving a response from the node."""
        url = self.api_object_url + 'response/'
        response = await self._get(url)
        return response

    @property
    async def completed(self) -> bool:
        """Check that task is completed."""
        response = await self.check()
        return response.value == 'SUCCESS'
