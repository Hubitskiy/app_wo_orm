from attr import attrs

from core.usecases import BaseUseCase

from users.services import CreateUserService


@attrs(auto_attribs=True)
class CreateUserUseCase(BaseUseCase):
    _create_user: CreateUserService

    async def validate(self):
        pass

    async def execute(self, **user_data):

        result = await self._create_user(**user_data)

        return result
