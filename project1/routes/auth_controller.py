from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException,Body,Header
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from project1.services.auth_service import ACCESS_TOKEN_EXPIRE_MINUTES, AuthService,SECRET_KEY,ALGORITHM
from project1.services.auth_service import AuthService
from project1.schemas.auth_schema import Token, UserLogin,UserCreate
from project1.models.user import User
from jose import JWTError, jwt
from project1.Database.MSDatabase import get_db
from project1.Database.dbmodels import Users

router = APIRouter()
auth_service = AuthService()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register",tags=['Register'])
async def register(user:UserCreate,db:Session=Depends(get_db)):
    hashed_password=auth_service.get_password_hash(user.password)
    db_user=Users(username=user.username,hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return{"Message":"user registered successfully"}

@router.post("/login", response_model=Token,tags=['Login'])
def login_for_access_token(username:str =Body(...), password:str=Body(...),db:Session=Depends(get_db)):#form_data:OAuth2PasswordRequestForm=Depends()
    user = auth_service.authenticate_user(username, password,db)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}




