from typing import Awaitable
from abc import abstractmethod


class BaseRetrieveHandler:

    @abstractmethod
    async def retrieve(self):
        pass

    async def __call__(self, *args, **kwargs):
        await self.retrieve()


class BaseRetrieveListHandler:

    @abstractmethod
    async def list_retrieve(self):
        pass

    async def __call__(self, *args, **kwargs):
        result = await self.list_retrieve()
        return result


class BaseCreateHandler:

    @abstractmethod
    async def create(self):
        pass

    async def __call__(self, *args, **kwargs):
        result = await self.create()
        return result


class BaseUpdateHandler:

    @abstractmethod
    async def update(self):
        pass

    async def __call__(self, *args, **kwargs):
        result = await self.update()
        return result


class BaseDeleteHandler:

    @abstractmethod
    async def delete(self):
        pass

    async def __call__(self, *args, **kwargs):
        result = await self.delete()
        return result
