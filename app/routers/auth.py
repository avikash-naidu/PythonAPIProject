from .. import models, schemas, utils, oauth2
from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from ..database import get_db


#connectst router to main file
router = APIRouter(
    tags=['Authentication']
)

#login 
@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session= Depends(get_db)):

    #chects if email exitsts in db
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    #runs exception if not found or incorrect details
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"Invalid Credentials")
    
    #creates accesstoken if user details are correct
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token":  access_token, "token_type": "bearer"}
