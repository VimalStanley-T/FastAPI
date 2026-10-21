# Fastapi yoda main program athavathu enga iruinthu start aga poguthu apdingrathukana code dea write panna
# porm
from fastapi import FastAPI, Depends, HTTPException 
# Propertie (itha vechi than fastapi kana oru app create panna porom,
# Intha app apdingrathu oru object, intha object vechi than fastapi framework work aaga poguthu) 
from schemas import Todo as TodoSchemas, TodoCreate
from sqlalchemy.orm import Session # this is class
from database import SessionLocal, Base, engine
from models import Todo

Base.metadata.create_all(bind=engine) #propertie
app = FastAPI()

# Dependancy for DB session
def get_db():
    db = SessionLocal() # SessionLocal function na call panrom
    try:
        yield db # db session kedachathum atha return panrom(return as yield)
    finally:
        db.close() 

# Route create panna porom
# POST - Create TODO Task
@app.post("/todos", response_model= TodoSchemas) # @app ithu vanthu oru Aneataion
# def create(todo: TodoSchemas, db: Session = Depends(get_db)):
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit() # model kana data db la store aaga intha db.commit() call panrom
    db.refresh(db_todo) # table la iruinthu id value va get panna intha db.refresh() call panrom
    return db_todo 

# GET - ALL Todos
@app.get("/todos", response_model=list[TodoSchemas])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# GET - get Single todo. # Nama get panna porathu single data so id kaittayom vennum. 
@app.get("/todos/{todo_id}", response_model=TodoSchemas) 
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# PUT - Update Todo
@app.put("/todos/{todo_id}", response_model=TodoSchemas)
def update_todo(todo_id:int, updated: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

# DELETE - Delete Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo Deleted Successfully"}