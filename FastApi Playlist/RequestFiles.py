
from fastapi import FastAPI, File, UploadFile,Form


app= FastAPI()

@app.post("/files/")
async def creat_file(files:list[bytes]=File(...,description="A file read as Bytes")):
    return {"file":[len(file) for file in files]}

@app.post("/uploadfile/")
async def creat_upload_file(files:list[UploadFile]=File(...,description="A File read as UploadFile")):
    contents = await file.read()
    return{"filename":[file.filename for file in files]}

#Combining Request Forms And Files:

@app.post("/file/")
async def creat_file(
        file:bytes=File(...),fileb:UploadFile=File(...),token:str=Form(...),
):
    return{
        "file size":len(file),
        "token":token,
        "fileb_content_type": fileb.content_type,
    }
