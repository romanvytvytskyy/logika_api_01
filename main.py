from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import *
from database import *
from crud import *
from models import *


app =FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_user")
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user    

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)