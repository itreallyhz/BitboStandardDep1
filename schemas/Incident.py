from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel, constr
from datetime import datetime

from typing import Optional
class IncidentSchema(BaseModel):
    case_title: constr(min_length=1, max_length=100)
    case_description: constr(min_length=1, max_length=100)
    complainant: constr(min_length=1, max_length=100)
    witness: Optional[constr(min_length=1, max_length=10)] = None
    officer: Optional[constr(min_length=1, max_length=100)] = None
    subject_complaint: Optional[constr(min_length=1, max_length=100)] = None
    place: Optional[constr(min_length=1, max_length=100)] = None
    happened: Optional[constr(min_length=1, max_length=100)] = None
    status: Optional[constr(min_length=1, max_length=100)] = None
    photo_path: UploadFile




