from sqlalchemy.orm import relationship


from config.database import Base
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

import uuid

class ResidentProfile(Base):
    __tablename__ = "residentprofiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=True)
    first_name = Column(String(50), nullable=True)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    suffix = Column(String(5), nullable=True)
    age = Column(String(50), nullable=True)
    birthday = Column(String(50), nullable=True)
    birth_order = Column(String(50), nullable=True)
    birthplace = Column(String(50), nullable=True)
    blood_type = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    civil_status = Column(String(10), nullable=True)
    house_no = Column(String(50), nullable=True)
    street = Column(String(50), nullable=True)
    phone_no = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    occupation = Column(String(50), nullable=True)

    # For Students
    st_school = Column(String(50), nullable=True)
    school_type = Column(String(50), nullable=True)
    st_place_of_school = Column(String(50), nullable=True)
    grade_level = Column(String(50), nullable=True)
    st_degree = Column(String(50), nullable=True)
    course = Column(String(50), nullable=True)

    # For Employee
    educational_attainment = Column(String(50), nullable=True)
    emp_school = Column(String(50), nullable=True)
    emp_place_of_school = Column(String(50), nullable=True)
    emp_degree = Column(String(50), nullable=True)
    company = Column(String(50), nullable=True)
    position = Column(String(50), nullable=True)
    salary = Column(String(50), nullable=True)
    years_employed = Column(String(50), nullable=True)

    ethnicity = Column(String(50), nullable=True)
    religion = Column(String(50), nullable=True)

    is_indigenous = Column(String(10), nullable=True)
    indigenous_type = Column(String(50), nullable=True)

    is_disability = Column(String(10), nullable=True)
    disability = Column(String(50), nullable=True)

    is_solo_parent = Column(String(50), nullable=True)

    # For Voters
    is_registered_voter = Column(String(10), nullable=True)
    precint_no = Column(String(50), nullable=True)

    SSS_no = Column(String(50), nullable=True)
    GSIS_no = Column(String(50), nullable=True)
    TIN_no = Column(String(50), nullable=True)

    valid_id = Column(String(10), nullable=True)

    # Mother's Information
    m_first_name = Column(String(50), nullable=True)
    m_middle_name = Column(String(50), nullable=True)
    m_last_name = Column(String(50), nullable=True)
    m_suffix = Column(String(5), nullable=True)
    m_blk = Column(String(50), nullable=True)
    m_street = Column(String(50), nullable=True)
    m_birthday = Column(String(50), nullable=True)
    m_gender = Column(String(50), nullable=True)
    m_phone_no = Column(String(50), nullable=True)
    m_email = Column(String(50), nullable=True)

    # Father's Information
    f_first_name = Column(String(50), nullable=True)
    f_middle_name = Column(String(50), nullable=True)
    f_last_name = Column(String(50), nullable=True)
    f_suffix = Column(String(5), nullable=True)
    f_blk = Column(String(50), nullable=True)
    f_street = Column(String(50), nullable=True)
    f_birthday = Column(String(50), nullable=True)
    f_gender = Column(String(50), nullable=True)
    f_phone_no = Column(String(50), nullable=True)
    f_email = Column(String(50), nullable=True)

    # Mandatory tables
    created_at = Column(DateTime, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_at = Column(DateTime, nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(UUID(as_uuid=True), nullable=True)


#Relationship
#pinaka unang relationship
#resident_household = relationship("HouseholdProfile", back_populates="household_resident")
#resident_personnel = relationship("Personnel", back_populates="personnel_resident")
