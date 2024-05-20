from fastapi import FastAPI
from project1.routes.item_controller import router as item_router
from project1.routes.auth_controller import router as auth_router
import uvicorn


app = FastAPI(title="LOGIN VERIFICATION & JWT AUTHORIZATION")


app.include_router(item_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)