from pydantic import BaseModel, Field


class CreateUserSerializer(BaseModel):

    email: str = Field(...)

    first_name: str = Field(...)

    last_name: str = Field(...)

    password: str = Field(...)
