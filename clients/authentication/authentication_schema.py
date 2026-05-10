from pydantic import BaseModel, Field, EmailStr
from tools.fakers import fake

class TokenSchema(BaseModel):
    """
    Описание структуры аутентификации токеновю
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)

class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификациию
    """
    token: TokenSchema
