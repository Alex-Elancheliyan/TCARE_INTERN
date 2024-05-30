from fastapi import FastAPI, Query, HTTPException
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date
from fastapi.responses import FileResponse
from io import BytesIO
import uvicorn

Base = declarative_base()

#TABLE MODELS
class BankDeposit(Base):
    __tablename__ = 'bank_deposit'

    Id = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    Type = Column(String(50))
    Amount = Column(Float, nullable=False)
    Deposit_Mode = Column(String(50))
    Remaining_Amount = Column(Float, nullable=False)
    Terminal_Id = Column(Integer, nullable=False)
    Merchant_Id = Column(Integer, nullable=False)

class PettyCash(Base):
    __tablename__ = 'petty_cash'

    Id = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    Description = Column(String(300), nullable=False)
    Amount = Column(Float, nullable=False)
    Balance_Amount = Column(Float, nullable=False)
    Terminal_Id = Column(Integer, nullable=False)
    Merchant_Id = Column(Integer, nullable=False)

app = FastAPI(title="All Books Download")


DB_USER = 'root'
DB_PASSWORD = 'alex1234'
DB_HOST = 'localhost'
DB_NAME = 'axdatabase'

SQLALCHEMY_DATABASE_URL = "MYSQL DB URL"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def download_books(table_name: str = Query(None), all_tables: bool = Query(False)):
    if all_tables:
        metadata = MetaData()
        metadata.reflect(bind=engine)
        with engine.connect() as conn:
            writer = pd.ExcelWriter("all_tables.xlsx")
            for table_name in metadata.tables.keys():
                table = metadata.tables[table_name]
                df = pd.read_sql_table(table_name, conn)
                df.to_excel(writer, sheet_name=table_name, index=False)
            #writer.save()
            writer.close()

            return FileResponse("all_tables.xlsx", filename="all_tables.xlsx",
                                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        return {"message": "All tables downloaded successfully as a single Excel file."}

    elif table_name:
        table_class = globals().get(table_name)
        if table_class:
            with SessionLocal() as session:
                query = session.query(table_class)
                df = pd.read_sql(query.statement, query.session.bind)
                df.to_excel(f"{table_name}.xlsx", index=False)
                return FileResponse("all_tables.xlsx", filename="all_tables.xlsx",
                                    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            return {"message": f"Table '{table_name}' downloaded successfully."}
        else:
            raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")
    else:
        raise HTTPException(status_code=400, detail="Either provide a specific table name or set 'all_tables' to True.")

@app.get("/download-books/")
async def download_books_endpoint(
        table_name: str = Query(None),
        all_tables: bool = Query(False)
):
    return download_books(table_name, all_tables)

if __name__ == "__main__":
    uvicorn.run("AllBooksDownload:app", host="127.0.0.1", port=8000, reload=True)
