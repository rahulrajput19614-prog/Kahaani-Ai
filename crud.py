from sqlalchemy.orm import Session
import models, schemas, security

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        username=user.username,
        auth_provider='email'
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user

def create_story(db: Session, story: dict, user: models.User):
    user.credits_remaining -= 1
    db_story = models.Story(
        title=story['title'],
        content=story['content'],
        cover_image_url=story['cover_image_url'],
        author_id=user.id
    )
    db.add(db_story)
    db.add(user)
    db.commit()
    db.refresh(db_story)
    return db_story

# ... Other CRUD functions for stories
