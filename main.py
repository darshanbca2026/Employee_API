from security import get_current_user
from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from security import create_access_token
from security import verify_password
from fastapi.security import OAuth2PasswordRequestForm
import crud
import model
import schemas
from database import SessionLocal, engine,Base
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import session
from security import authenticate_user, create_access_token
app = FastAPI()
@app.get("/")
def home():
    return {"message": "API Running 🚀", "go_to_docs": "/docs"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    db_user = db.query(model.User).filter(
        model.User.username == user.username
    ).first()

    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return crud.create_user(db, user)
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(model.User).filter(
        model.User.username == form_data.username
    ).first()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": form_data.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/employees", response_model=schemas.Employee)
def create_employee(
    employee:
 schemas.EmployeeCreate,
    db: Session = Depends(get_db),
      current_user = Depends(get_current_user)

):
    return crud.create_employee(db, employee)
@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(
    employee_id: int,
    db: Session = Depends(get_db), current_user = Depends(get_current_user)
):
    employee = crud.get_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated = crud.update_employee(db, employee_id, employee)
    if updated is None:
        raise HTTPException(status_code = 404, detail="Employee not found")
    return updated

@app.delete("/employees/{employee_id}")
def delete_employee(
  employee_id: int,
  db: Session = Depends(get_db),
  current_user = Depends(get_current_user)
 ):
 db_employee = crud.delete_employee(db, employee_id)
 if db_employee is None:
    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

   