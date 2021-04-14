from attr import attrs

from core.handlers import BaseCreateHandler
from core.containers import resolve

from users.usecases import CreateUserUseCase
from users.serializers import CreateUserSerializer


@attrs(auto_attribs=True)
class CreateUserHandler(BaseCreateHandler):

    user_data: CreateUserSerializer

    async def create(self):

        create_user = resolve(CreateUserUseCase)

        user = await create_user(**self.user_data.dict())

        return user
