from pydantic import BaseModel, constr
from typing import Optional
from fastapi import UploadFile
from datetime import datetime

class PersonnelSchema(BaseModel):
    first_name: constr(min_length=1, max_length=100)
    middle_name: constr(min_length=1, max_length=100)
    last_name: constr(min_length=1, max_length=100)
    suffix: Optional[constr(min_length=1, max_length=100)] = None
    birthday: Optional[constr(min_length=1, max_length=100)] = None
    email: Optional[constr(min_length=1, max_length=100)] = None
    contact_no: Optional[constr(min_length=1, max_length=100)] = None
    position: Optional[constr(min_length=1, max_length=100)] = None
    photo_path: UploadFile



