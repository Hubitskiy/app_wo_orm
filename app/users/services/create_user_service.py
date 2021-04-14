from attr import attrs

from core.usecases import BaseService


@attrs(auto_attribs=True)
class CreateUserService(BaseService):

    async def __call__(self, first_name: str, last_name: str, email: str, password: str,*args, **kwargs):
        return {
            "email": "new " + email,
            "last_name": "new " + last_name,
            "first_name": "new " + first_name
        }
