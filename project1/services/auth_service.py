from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import HTTPException
from project1.models.user import User
from project1.schemas.auth_schema import Token, UserLogin
from mysql import connector
from project1.Database.MSDatabase import get_db
from project1.Database.dbmodels import Users

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class AuthService:

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def authenticate_user(self, username: str, password: str,db:Session) -> User:
        user = db.query(Users).filter(Users.username == username).first()
        if not user or not self.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        db.close()
        return user

    async def get_current_user(token: str = Depends(oauth2_scheme)):
        credentials_exceptions = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exceptions
            token_data = Token(username=token_data.username)

        except JWTError:
            raise credentials_exceptions
            user = get_user(username=token_data.username)
            if user is None:
                raise credentials_exceptions
            return user
