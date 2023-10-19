from typing import Union

from fastapi import Depends,FastAPI, HTTPException
from typing_extensions import Annotated

from . import crud,schemas
from .database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Userを登録
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# async def create_user(todo_in: TodoIn,  db: Session = Depends(get_db)):
#     todo = Todo(title=todo_in.title, done=False)
#     db.add(todo)
#     db.commit()
#     todo = get_todo(db, todo.id)
#     return todo

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
