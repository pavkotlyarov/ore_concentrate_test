from dotenv import dotenv_values
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

env_settings = dotenv_values('.env')

DATABASE_URL = 'postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}'.format(
    username=env_settings['POSTGRES_USER'],
    password=env_settings['POSTGRES_PASSWORD'],
    host=env_settings['POSTGRES_HOST'],
    port=env_settings['POSTGRES_PORT'],
    db_name=env_settings['POSTGRES_NAME']
)
SECRET_KEY = env_settings['SECRET_KEY']
HASH_ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
