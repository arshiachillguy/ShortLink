from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

#creat table in database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/shorten" , response_model=schemas.URl)
def create_short_url(url:schemas.URLCreate):
    url : schemas.URLCreate
    db : Session = Depends(get_db())
    db_url = crud.create_short_url(db=db , original_url=url.original_url)
    return db_url

@app.get("/{short_code}")
def redirect_to_original(short_code: str):
    db = next(get_db())
    db_url = crud.get_url_by_short_code(db=db, short_code=short_code)

    if not db_url:
        raise HTTPException(status_code=404 , detail="url not found i'm sorry.")

    return {"original_url" : db_url.original_url}













