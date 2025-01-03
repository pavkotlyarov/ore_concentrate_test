from pydantic import BaseModel


class User(BaseModel):
    username: str

class DatabaseUser(User):
    password: str
