from fastapi import FastAPI,Cookie, Header

app = FastAPI()

@app.get("/items")
async def read_items(
        cookie_id:str | None=Cookie(None),
        accept_encoding: str | None = Header(None),
        sec_ch_ua: str | None=Header(None),
        user_agent: str | None = Header(None),
):

    return {
        "cookie_id":cookie_id,
        "Accept_Encoding": accept_encoding,
        "sec_ch_ua": sec_ch_ua,
        "User_Agent":user_agent,
    }
