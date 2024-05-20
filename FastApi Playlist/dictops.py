from fastapi import FastAPI , HTTPException

app = FastAPI()

dict1={}

@app.get("/items")
async def items():
 return {"My Dictionary":dict1}

@app.post("/items/{item_id}")
async def post_items(item_id:int, item_data:int):
 dict1[item_id]=item_data
 return {"Item ID":item_id,"Item Data":item_data}

@app.put("/update/{item_id}")
async def update_items(item_data:int,item_id:int):
  dict1.update({item_id:item_data})
  return {f"{item_id}is successfully updated "}

@app.delete("/delete_item/{item_id}")
async def delete_item(item_id:int):
  try:
   deleted_item=dict1.pop(item_id)
   return {f" Item from {item_id} is deleted successfully"}
  except KeyError:
   raise HTTPException(status_code=404, detail="Key Not Found")


