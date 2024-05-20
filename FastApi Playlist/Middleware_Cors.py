from fastapi import FastAPI,Request

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime,timedelta
import time
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn


app=FastAPI()


class MyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


#origins = ["http://localhost:8000", "http://localhost:3000"]
app.add_middleware(MyMiddleware)
#app.add_middleware(CORSMiddleware, allow_origins=origins)

@app.get("/item")
async def get_item():
    return {"Item_Name": "Pepsi"}


if __name__ == '__main__':
    uvicorn.run("Middleware_Cors:app", host="127.0.0.1", port=8000,reload=True)