from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timedelta, timezone
from jose import jwt
from settings import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, HASH_ALGORITHM, pwd_context
from .base import Base

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    @staticmethod
    def hash_password(password: str):
        return pwd_context.hash(password)

    def validate_password(self, password: str):
        return pwd_context.verify(password, self.password)

    def create_access_token(self):
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        encoded_jwt = jwt.encode({'username': self.username}, SECRET_KEY, algorithm=HASH_ALGORITHM)
        return encoded_jwt
