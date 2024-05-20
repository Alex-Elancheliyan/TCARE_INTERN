from fastapi import FastAPI , HTTPException

app = FastAPI()

list1=[]

@app.get("/items")
async def get_items():
 return {"My List":list1}

@app.post("/items/{item_id}")
async def post_items(item_id:int):
 list1.append(item_id)
 return {f"{item_id} added successfully"}

@app.put("/update/{index}")
async def update_items(index:int,item_id:int):
 try:
  list1[index]=item_id
  return {f"{item_id}is successfully updated at {index} "}
 except IndexError:
  raise HTTPException(status_code=404, detail="Item index out of range")

@app.delete("/delete_item/{index}")
async def delete_item(index:int):
  try:
   deleted_item=list1.pop(index)
   return {f"Item from index no {index} is deleted successfully"}
  except IndexError:
   raise HTTPException(status_code=404, detail="Item index out of range")
