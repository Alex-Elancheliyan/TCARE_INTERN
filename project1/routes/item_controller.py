from fastapi import APIRouter, HTTPException
from typing import List
from project1.services.item_services import ItemService
from project1.schemas.item_schema import ItemCreate, ItemUpdate
from project1.models.item import Item
from project1.models.user import User
#AX
from fastapi import Depends
from project1.services.auth_service import AuthService
from project1.routes.auth_controller import oauth2_scheme
from jose import JWTError, jwt
from project1.services.auth_service import SECRET_KEY,ALGORITHM
from fastapi import Security
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

router = APIRouter(tags=['Authorized Endpoints'])
item_service = ItemService()
auth_service = AuthService()
bearer_scheme = HTTPBearer()

def verify_token(token: HTTPAuthorizationCredentials= Security(bearer_scheme)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        sub = payload.get("sub")
        if sub is None:
            raise HTTPException(status_code=403, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return True

@router.get("/items", response_model=List[Item])
def read_items(authdep=Depends(verify_token)):
    return item_service.get_all_items()

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int,authdep=Depends(verify_token)):
    item = item_service.get_item_by_id(item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@router.post("/items", response_model=Item)
def create_item(item_data: ItemCreate,authdep=Depends(verify_token)):#, User=Depends(verify_token)):
    return item_service.create_item(item_data)

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemUpdate, authdep=Depends(verify_token)):
    updated_item = item_service.update_item(item_id, item_data)
    if updated_item:
        return updated_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}")
def delete_item(item_id: int, authdep=Depends(verify_token)):
    if item_service.delete_item(item_id):
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
