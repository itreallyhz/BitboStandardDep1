from typing import Optional
from pydantic import BaseModel, constr
from uuid import UUID
from datetime import datetime


class ResidentProfileSchema(BaseModel):
    first_name: Optional[constr(min_length=0, max_length=50)] = None
    middle_name: Optional[constr(min_length=0, max_length=50)] = None
    last_name: Optional[constr(min_length=0, max_length=50)] = None
    suffix: Optional[constr(max_length=5)] = None
    age: Optional[constr(min_length=0, max_length=50)] = None
    birthday: Optional[constr(min_length=0, max_length=50)] = None
    birth_order: Optional[constr(min_length=0, max_length=50)] = None
    birthplace: Optional[constr(min_length=0, max_length=50)] = None
    blood_type: Optional[constr(max_length=50)] = None
    gender: Optional[constr(min_length=0, max_length=50)] = None
    civil_status: Optional[constr(min_length=0, max_length=10)] = None
    house_no: Optional[constr(min_length=0, max_length=50)] = None
    street: Optional[constr(min_length=0, max_length=50)] = None
    phone_no: Optional[constr(min_length=0, max_length=50)] = None
    email: Optional[constr(min_length=0, max_length=50)] = None
    occupation: Optional[constr(min_length=0, max_length=50)] = None

    st_school: Optional[constr(min_length=0, max_length=50)] = None
    school_type: Optional[constr(min_length=0, max_length=50)] = None
    st_place_of_school: Optional[constr(min_length=0, max_length=50)] = None
    grade_level: Optional[constr(min_length=0, max_length=50)] = None
    st_degree: Optional[constr(min_length=0, max_length=50)] = None
    course: Optional[constr(min_length=0, max_length=50)] = None

    educational_attainment: Optional[constr(min_length=0, max_length=50)] = None
    emp_school: Optional[constr(min_length=0, max_length=50)] = None
    emp_place_of_school: Optional[constr(min_length=0, max_length=50)] = None
    emp_degree: Optional[constr(min_length=0, max_length=50)] = None
    company: Optional[constr(min_length=0, max_length=50)] = None
    position: Optional[constr(min_length=0, max_length=50)] = None
    salary: Optional[constr(min_length=0, max_length=50)] = None
    years_employed: Optional[constr(min_length=0, max_length=50)] = None

    ethnicity: Optional[constr(min_length=0, max_length=50)] = None
    religion: Optional[constr(min_length=0, max_length=50)] = None

    is_indigenous: Optional[constr(min_length=0, max_length=10)] = None
    indigenous_type: Optional[constr(min_length=0, max_length=50)] = None

    is_disability: Optional[constr(min_length=0, max_length=10)] = None
    disability: Optional[constr(min_length=0, max_length=50)] = None

    is_solo_parent: Optional[constr(min_length=0, max_length=50)] = None

    is_registered_voter: Optional[constr(min_length=0, max_length=10)] = None
    precint_no: Optional[constr(min_length=0, max_length=50)] = None

    SSS_no: Optional[constr(min_length=0, max_length=50)] = None
    GSIS_no: Optional[constr(min_length=0, max_length=50)] = None
    TIN_no: Optional[constr(min_length=0, max_length=50)] = None

    valid_id: Optional[constr(min_length=0, max_length=10)] = None

    m_first_name: Optional[constr(min_length=0, max_length=50)] = None
    m_middle_name: Optional[constr(min_length=0, max_length=50)] = None
    m_last_name: Optional[constr(min_length=0, max_length=50)] = None
    m_suffix: Optional[constr(max_length=5)] = None
    m_blk: Optional[constr(min_length=0, max_length=50)] = None
    m_street: Optional[constr(min_length=0, max_length=50)] = None
    m_birthday: Optional[constr(min_length=0, max_length=50)] = None
    m_gender: Optional[constr(min_length=0, max_length=50)] = None
    m_phone_no: Optional[constr(min_length=0, max_length=50)] = None
    m_email: Optional[constr(min_length=0, max_length=50)] = None

    f_first_name: Optional[constr(min_length=0, max_length=50)] = None
    f_middle_name: Optional[constr(min_length=0, max_length=50)] = None
    f_last_name: Optional[constr(min_length=0, max_length=50)] = None
    f_suffix: Optional[constr(max_length=5)] = None
    f_blk: Optional[constr(min_length=0, max_length=50)] = None
    f_street: Optional[constr(min_length=0, max_length=50)] = None
    f_birthday: Optional[constr(min_length=0, max_length=50)] = None
    f_gender: Optional[constr(min_length=0, max_length=50)] = None
    f_phone_no: Optional[constr(min_length=0, max_length=50)] = None
    f_email: Optional[constr(min_length=0, max_length=50)] = None


