from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel, constr
from datetime import datetime

from typing import Optional
class BarangayOfficialSchema(BaseModel):
    first_name: constr(min_length=1, max_length=100)
    middle_name: constr(min_length=1, max_length=100)
    last_name: constr(min_length=1, max_length=100)
    suffix: Optional[constr(min_length=1, max_length=10)] = None
    birthday: Optional[constr(min_length=1, max_length=100)] = None
    email: Optional[constr(min_length=1, max_length=100)] = None
    contact_no: Optional[constr(min_length=1, max_length=100)] = None
    position: Optional[constr(min_length=1, max_length=100)] = None
    start_term: Optional[constr(min_length=1, max_length=100)] = None
    end_term:  Optional[constr(min_length=1, max_length=100)] = None
    photo_path: UploadFile




