from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud, security
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KahaaniAI API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# All the API endpoints for register, login, story generation, and story management go here...
# (The complete code from our previous conversations)
@app.post("/register/")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Register logic...
    return crud.create_user(db=db, user=user)

@app.post("/login/")
def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    # Login logic...
    user = crud.authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# ... other endpoints for stories ...
