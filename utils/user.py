from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import SECRET_KEY, HASH_ALGORITHM, oauth2_scheme
from database import get_session
from models import User
from schemas import TokenData, User as UserSchema


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Authentication failed',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        username: str = payload.get('username')

        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = session.scalars(select(User).where(User.username == token_data.username)).one()

    if user is None:
        raise credential_exception

    return UserSchema(username=user.username)
