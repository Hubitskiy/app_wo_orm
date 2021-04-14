from typing import Any, Awaitable


class BaseUseCase:

    async def validate(self, *args, **kwargs) -> Any:
        pass

    async def execute(self, *args, **kwargs) -> Awaitable:
        pass

    async def __call__(self, *args, **kwargs):

        await self.validate()

        result = await self.execute(*args, **kwargs)

        return result


class BaseService:
    pass
