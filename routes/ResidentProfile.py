from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.ResidentProfile import ResidentProfile
from models.User import User
from schemas.ResidentProfile import ResidentProfileSchema
from schemas.User import UserSchema
from auth.Oauth2 import get_current_user
from datetime import datetime
from pydantic import UUID4
from sqlalchemy import or_

router = APIRouter(prefix="/residentprofiles", tags=["Resident Profile"])

# Get All residents
@router.get("/get")
async def index(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    # Query all residents that are not marked as deleted
    residents = db.query(ResidentProfile).filter(ResidentProfile.deleted_at == None).all()
    data = []

    if residents:
        for resident in residents:
            data.append({
                "id": resident.id,
                "first_name": resident.first_name,
                "middle_name": resident.middle_name,
                "last_name": resident.last_name,
                "suffix": resident.suffix,
                "age": resident.age,
                "birthday": resident.birthday,
                "birth_order": resident.birth_order,
                "birthplace": resident.birthplace,
                "blood_type": resident.blood_type,
                "gender": resident.gender,
                "civil_status": resident.civil_status,
                "house_no": resident.house_no,
                "street": resident.street,
                "phone_no": resident.phone_no,
                "email": resident.email,
                "occupation": resident.occupation,
                "st_school": resident.st_school,
                "school_type": resident.school_type,
                "st_place_of_school": resident.st_place_of_school,
                "grade_level": resident.grade_level,
                "st_degree": resident.st_degree,
                "course": resident.course,
                "educational_attainment": resident.educational_attainment,
                "emp_school": resident.emp_school,
                "emp_place_of_school": resident.emp_place_of_school,
                "emp_degree": resident.emp_degree,
                "company": resident.company,
                "position": resident.position,
                "salary": resident.salary,
                "years_employed": resident.years_employed,
                "ethnicity": resident.ethnicity,
                "religion": resident.religion,
                "is_indigenous": resident.is_indigenous,
                "indigenous_type": resident.indigenous_type,
                "is_disability": resident.is_disability,
                "disability": resident.disability,
                "is_solo_parent": resident.is_solo_parent,
                "is_registered_voter": resident.is_registered_voter,
                "precint_no": resident.precint_no,
                "SSS_no": resident.SSS_no,
                "GSIS_no": resident.GSIS_no,
                "TIN_no": resident.TIN_no,
                "valid_id": resident.valid_id,
                "m_first_name": resident.m_first_name,
                "m_middle_name": resident.m_middle_name,
                "m_last_name": resident.m_last_name,
                "m_suffix": resident.m_suffix,
                "m_blk": resident.m_blk,
                "m_street": resident.m_street,
                "m_birthday": resident.m_birthday,
                "m_gender": resident.m_gender,
                "m_phone_no": resident.m_phone_no,
                "m_email": resident.m_email,
                "f_first_name": resident.f_first_name,
                "f_middle_name": resident.f_middle_name,
                "f_last_name": resident.f_last_name,
                "f_suffix": resident.f_suffix,
                "f_blk": resident.f_blk,
                "f_street": resident.f_street,
                "f_birthday": resident.f_birthday,
                "f_gender": resident.f_gender,
                "f_phone_no": resident.f_phone_no,
                "f_email": resident.f_email,
                "created_at": resident.created_at,
                "created_by": resident.created_by,
                "updated_at": resident.updated_at,
                "updated_by": resident.updated_by
            })
        return {
            "message": "Residents fetched successfully",
            "data": data
       }
    else:
        raise HTTPException(status_code=404, detail="Residents not found")

#Get All Residents | Pagination

@router.get("/getp")
async def index(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: UserSchema = Depends(get_current_user)):

    # Calculate the offset based on the page and limit
    offset = (page - 1) * limit

    # Query residents with pagination and search
    query = db.query(ResidentProfile).filter(ResidentProfile.deleted_at == None)

    if search:
        # Use OR condition to search in multiple columns
        query = query.filter(
            or_(
                ResidentProfile.first_name.ilike(f"%{search}%"),
                ResidentProfile.last_name.ilike(f"%{search}%"),
                ResidentProfile.house_no.ilike(f"%{search}%"),
                ResidentProfile.street.ilike(f"%{search}%"),
                # Add more columns as needed
            )
        )

    residents = query.offset(offset).limit(limit).all()

    data = []

    if residents:
        for resident in residents:
            data.append({
                "id": resident.id,
                "first_name": resident.first_name,
                "middle_name": resident.middle_name,
                "last_name": resident.last_name,
                "suffix": resident.suffix,
                "age": resident.age,
                "birthday": resident.birthday,
                "birth_order": resident.birth_order,
                "birthplace": resident.birthplace,
                "blood_type": resident.blood_type,
                "gender": resident.gender,
                "civil_status": resident.civil_status,
                "house_no": resident.house_no,
                "street": resident.street,
                "phone_no": resident.phone_no,
                "email": resident.email,
                "occupation": resident.occupation,
                "st_school": resident.st_school,
                "school_type": resident.school_type,
                "st_place_of_school": resident.st_place_of_school,
                "grade_level": resident.grade_level,
                "st_degree": resident.st_degree,
                "course": resident.course,
                "educational_attainment": resident.educational_attainment,
                "emp_school": resident.emp_school,
                "emp_place_of_school": resident.emp_place_of_school,
                "emp_degree": resident.emp_degree,
                "company": resident.company,
                "position": resident.position,
                "salary": resident.salary,
                "years_employed": resident.years_employed,
                "ethnicity": resident.ethnicity,
                "religion": resident.religion,
                "is_indigenous": resident.is_indigenous,
                "indigenous_type": resident.indigenous_type,
                "is_disability": resident.is_disability,
                "disability": resident.disability,
                "is_solo_parent": resident.is_solo_parent,
                "is_registered_voter": resident.is_registered_voter,
                "precint_no": resident.precint_no,
                "SSS_no": resident.SSS_no,
                "GSIS_no": resident.GSIS_no,
                "TIN_no": resident.TIN_no,
                "valid_id": resident.valid_id,
                "m_first_name": resident.m_first_name,
                "m_middle_name": resident.m_middle_name,
                "m_last_name": resident.m_last_name,
                "m_suffix": resident.m_suffix,
                "m_blk": resident.m_blk,
                "m_street": resident.m_street,
                "m_birthday": resident.m_birthday,
                "m_gender": resident.m_gender,
                "m_phone_no": resident.m_phone_no,
                "m_email": resident.m_email,
                "f_first_name": resident.f_first_name,
                "f_middle_name": resident.f_middle_name,
                "f_last_name": resident.f_last_name,
                "f_suffix": resident.f_suffix,
                "f_blk": resident.f_blk,
                "f_street": resident.f_street,
                "f_birthday": resident.f_birthday,
                "f_gender": resident.f_gender,
                "f_phone_no": resident.f_phone_no,
                "f_email": resident.f_email,
                "created_at": resident.created_at,
                "created_by": resident.created_by,
                "updated_at": resident.updated_at,
                "updated_by": resident.updated_by
            })

        return {
            "message": "Residents fetched successfully",
            "data": data,
            "page": page,
            "limit": limit
        }
    else:
        raise HTTPException(status_code=404, detail="Residents not found")



# Get all Deleted Residents
@router.get("/deleted")
async def index(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    # Query all residents that are not marked as deleted
    residents = db.query(ResidentProfile).filter(ResidentProfile.deleted_at != None).all()
    data = []

    if residents:
        for resident in residents:
            data.append({
                "id": resident.id,
                "first_name": resident.first_name,
                "middle_name": resident.middle_name,
                "last_name": resident.last_name,
                "suffix": resident.suffix,
                "age": resident.age,
                "birthday": resident.birthday,
                "birth_order": resident.birth_order,
                "birthplace": resident.birthplace,
                "blood_type": resident.blood_type,
                "gender": resident.gender,
                "civil_status": resident.civil_status,
                "house_no": resident.house_no,
                "street": resident.street,
                "phone_no": resident.phone_no,
                "email": resident.email,
                "occupation": resident.occupation,
                "st_school": resident.st_school,
                "school_type": resident.school_type,
                "st_place_of_school": resident.st_place_of_school,
                "grade_level": resident.grade_level,
                "st_degree": resident.st_degree,
                "course": resident.course,
                "educational_attainment": resident.educational_attainment,
                "emp_school": resident.emp_school,
                "emp_place_of_school": resident.emp_place_of_school,
                "emp_degree": resident.emp_degree,
                "company": resident.company,
                "position": resident.position,
                "salary": resident.salary,
                "years_employed": resident.years_employed,
                "ethnicity": resident.ethnicity,
                "religion": resident.religion,
                "is_indigenous": resident.is_indigenous,
                "indigenous_type": resident.indigenous_type,
                "is_disability": resident.is_disability,
                "disability": resident.disability,
                "is_solo_parent": resident.is_solo_parent,
                "is_registered_voter": resident.is_registered_voter,
                "precint_no": resident.precint_no,
                "SSS_no": resident.SSS_no,
                "GSIS_no": resident.GSIS_no,
                "TIN_no": resident.TIN_no,
                "valid_id": resident.valid_id,
                "m_first_name": resident.m_first_name,
                "m_middle_name": resident.m_middle_name,
                "m_last_name": resident.m_last_name,
                "m_suffix": resident.m_suffix,
                "m_blk": resident.m_blk,
                "m_street": resident.m_street,
                "m_birthday": resident.m_birthday,
                "m_gender": resident.m_gender,
                "m_phone_no": resident.m_phone_no,
                "m_email": resident.m_email,
                "f_first_name": resident.f_first_name,
                "f_middle_name": resident.f_middle_name,
                "f_last_name": resident.f_last_name,
                "f_suffix": resident.f_suffix,
                "f_blk": resident.f_blk,
                "f_street": resident.f_street,
                "f_birthday": resident.f_birthday,
                "f_gender": resident.f_gender,
                "f_phone_no": resident.f_phone_no,
                "f_email": resident.f_email,
                "created_at": resident.created_at,
                "created_by": resident.created_by,
                "updated_at": resident.updated_at,
                "updated_by": resident.updated_by
            })
        return {
            "message": "Residents fetched successfully",
            "data": data
       }
    else:
        raise HTTPException(status_code=404, detail="Residents not found")


@router.post("/add")
async def store(request: ResidentProfileSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    user = db.query(User).filter(User.email == current_user.email).first()
    # Ensure user is authenticated
    if not user:
        raise HTTPException(status_code=404, detail="Not authenticated")
    # Retrieve user id from the authenticated user
    userid = user.id

    # Check if resident with the same first_name already exists
    #resident = db.query(ResidentProfile).filter(ResidentProfile.first_name == request.first_name).first()
    #if resident:
        #raise HTTPException(status_code=400, detail=f"Resident with name '{request.first_name}' already exists!")

    try:
        # Create a new ResidentProfile instance
        resident = ResidentProfile(
            first_name=request.first_name,
            middle_name=request.middle_name,
            last_name=request.last_name,
            suffix=request.suffix,
            age=request.age,
            birthday=request.birthday,
            birth_order=request.birth_order,
            birthplace=request.birthplace,
            blood_type=request.blood_type,
            gender=request.gender,
            civil_status=request.civil_status,
            house_no=request.house_no,
            street=request.street,
            phone_no=request.phone_no,
            email=request.email,
            occupation=request.occupation,
            st_school=request.st_school,
            school_type=request.school_type,
            st_place_of_school=request.st_place_of_school,
            grade_level=request.grade_level,
            st_degree=request.st_degree,
            course=request.course,
            educational_attainment=request.educational_attainment,
            emp_school=request.emp_school,
            emp_place_of_school=request.emp_place_of_school,
            emp_degree=request.emp_degree,
            company=request.company,
            position=request.position,
            salary=request.salary,
            years_employed=request.years_employed,
            ethnicity=request.ethnicity,
            religion=request.religion,
            is_indigenous=request.is_indigenous,
            indigenous_type=request.indigenous_type,
            is_disability=request.is_disability,
            disability=request.disability,
            is_solo_parent=request.is_solo_parent,
            is_registered_voter=request.is_registered_voter,
            precint_no=request.precint_no,
            SSS_no=request.SSS_no,
            GSIS_no=request.GSIS_no,
            TIN_no=request.TIN_no,
            valid_id=request.valid_id,
            m_first_name=request.m_first_name,
            m_middle_name=request.m_middle_name,
            m_last_name=request.m_last_name,
            m_suffix=request.m_suffix,
            m_blk=request.m_blk,
            m_street=request.m_street,
            m_birthday=request.m_birthday,
            m_gender=request.m_gender,
            m_phone_no=request.m_phone_no,
            m_email=request.m_email,
            f_first_name=request.f_first_name,
            f_middle_name=request.f_middle_name,
            f_last_name=request.f_last_name,
            f_suffix=request.f_suffix,
            f_blk=request.f_blk,
            f_street=request.f_street,
            f_birthday=request.f_birthday,
            f_gender=request.f_gender,
            f_phone_no=request.f_phone_no,
            f_email=request.f_email,
            created_at=datetime.now(),
            created_by=userid
        )
        db.add(resident)
        db.commit()

        # Return success message and data
        return {
            "message": "Resident successfully added!",
            "data": {
                "first_name": resident.first_name,
                "middle_name": resident.middle_name,
                "last_name": resident.last_name,
                #"civil_status": resident.civil_status,
                #"is_registered_voter": resident.is_registered_voter,
                "created_at": resident.created_at,
                "created_by": resident.created_by
            }
        }
    except Exception as e:
        # Rollback and raise exception in case of an error
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


#Get Specific Resident
@router.get("/{id}")
async def show(id: UUID4, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    resident = db.query(ResidentProfile).filter(ResidentProfile.id == id, ResidentProfile.deleted_at == None).first()

    if resident:
        return {
            "message": f"Resident: {resident.id} fetched successfully!",
            "data": {
                "id": resident.id,
                "first_name": resident.first_name,
                "middle_name": resident.middle_name,
                "last_name": resident.last_name,
                "suffix": resident.suffix,
                "age": resident.age,
                "birthday": resident.birthday,
                "birth_order": resident.birth_order,
                "birthplace": resident.birthplace,
                "blood_type": resident.blood_type,
                "gender": resident.gender,
                "civil_status": resident.civil_status,
                "house_no": resident.house_no,
                "street": resident.street,
                "phone_no": resident.phone_no,
                "email": resident.email,
                "occupation": resident.occupation,
                "st_school": resident.st_school,
                "school_type": resident.school_type,
                "st_place_of_school": resident.st_place_of_school,
                "grade_level": resident.grade_level,
                "st_degree": resident.st_degree,
                "course": resident.course,
                "educational_attainment": resident.educational_attainment,
                "emp_school": resident.emp_school,
                "emp_place_of_school": resident.emp_place_of_school,
                "emp_degree": resident.emp_degree,
                "company": resident.company,
                "position": resident.position,
                "salary": resident.salary,
                "years_employed": resident.years_employed,
                "ethnicity": resident.ethnicity,
                "religion": resident.religion,
                "is_indigenous": resident.is_indigenous,
                "indigenous_type": resident.indigenous_type,
                "is_disability": resident.is_disability,
                "disability": resident.disability,
                "is_solo_parent": resident.is_solo_parent,
                "is_registered_voter": resident.is_registered_voter,
                "precint_no": resident.precint_no,
                "SSS_no": resident.SSS_no,
                "GSIS_no": resident.GSIS_no,
                "TIN_no": resident.TIN_no,
                "valid_id": resident.valid_id,
                "m_first_name": resident.m_first_name,
                "m_middle_name": resident.m_middle_name,
                "m_last_name": resident.m_last_name,
                "m_suffix": resident.m_suffix,
                "m_blk": resident.m_blk,
                "m_street": resident.m_street,
                "m_birthday": resident.m_birthday,
                "m_gender": resident.m_gender,
                "m_phone_no": resident.m_phone_no,
                "m_email": resident.m_email,
                "f_first_name": resident.f_first_name,
                "f_middle_name": resident.f_middle_name,
                "f_last_name": resident.f_last_name,
                "f_suffix": resident.f_suffix,
                "f_blk": resident.f_blk,
                "f_street": resident.f_street,
                "f_birthday": resident.f_birthday,
                "f_gender": resident.f_gender,
                "f_phone_no": resident.f_phone_no,
                "f_email": resident.f_email,
                "created_at": resident.created_at,
                "created_by": resident.created_by,
                "updated_at": resident.updated_at,
                "updated_by": resident.updated_by,
                "deleted_at": resident.deleted_at,
                "deleted_by": resident.deleted_by
            }
        }
    else:
        raise HTTPException(status_code=404, detail=f"Resident does not exists!")


@router.put("/{id}")
async def update(id: UUID4, request: ResidentProfileSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    resident = db.query(ResidentProfile).filter(ResidentProfile.id == id, ResidentProfile.deleted_at == None).first()
    user = db.query(User).filter(User.email == current_user.email).first()
    #Ensure user is authenticated
    if not user:
        raise HTTPException(status_code=404, detail="Not authenticated")
    # Retrieve user id from the authenticated user
    userid = user.id

    if resident:
        resident.first_name = request.first_name
        resident.middle_name = request.middle_name
        resident.last_name = request.last_name
        resident.suffix = request.suffix
        resident.age = request.age
        resident.birthday = request.birthday
        resident.birth_order = request.birth_order
        resident.birthplace = request.birthplace
        resident.blood_type = request.blood_type
        resident.gender = request.gender
        resident.civil_status = request.civil_status
        resident.house_no = request.house_no
        resident.street = request.street
        resident.phone_no = request.phone_no
        resident.email = request.email
        resident.occupation = request.occupation
        resident.st_school = request.st_school
        resident.school_type = request.school_type
        resident.st_place_of_school = request.st_place_of_school
        resident.grade_level = request.grade_level
        resident.st_degree = request.st_degree
        resident.course = request.course
        resident.educational_attainment = request.educational_attainment
        resident.emp_school = request.emp_school
        resident.emp_place_of_school = request.emp_place_of_school
        resident.emp_degree = request.emp_degree
        resident.company = request.company
        resident.position = request.position
        resident.salary = request.salary
        resident.years_employed = request.years_employed
        resident.ethnicity = request.ethnicity
        resident.religion = request.religion
        resident.is_indigenous = request.is_indigenous
        resident.indigenous_type = request.indigenous_type
        resident.is_disability = request.is_disability
        resident.disability = request.disability
        resident.is_solo_parent = request.is_solo_parent
        resident.is_registered_voter = request.is_registered_voter
        resident.precint_no = request.precint_no
        resident.SSS_no = request.SSS_no
        resident.GSIS_no = request.GSIS_no
        resident.TIN_no = request.TIN_no
        resident.valid_id = request.valid_id
        resident.m_first_name = request.m_first_name
        resident.m_middle_name = request.m_middle_name
        resident.m_last_name = request.m_last_name
        resident.m_suffix = request.m_suffix
        resident.m_blk = request.m_blk
        resident.m_street = request.m_street
        resident.m_birthday = request.m_birthday
        resident.m_gender = request.m_gender
        resident.m_phone_no = request.m_phone_no
        resident.m_email = request.m_email
        resident.f_first_name = request.f_first_name
        resident.f_middle_name = request.f_middle_name
        resident.f_last_name = request.f_last_name
        resident.f_suffix = request.f_suffix
        resident.f_blk = request.f_blk
        resident.f_street = request.f_street
        resident.f_birthday = request.f_birthday
        resident.f_gender = request.f_gender
        resident.f_phone_no = request.f_phone_no
        resident.f_email = request.f_email
        resident.updated_at = datetime.now()
        resident.updated_by = userid
        db.commit()

        return {
            "message": f"Resident: {resident.id} updated successfully",
            "data": {
                "first_name": resident.first_name,
                "last_name": resident.last_name,
                "civil_status": resident.civil_status,
                "is_registered_voter": resident.is_registered_voter,
                "created_at": resident.created_at,
                "created_by": resident.created_by,
                "updated_at": resident.updated_at,
                "updated_by": resident.deleted_by
            }
        }
    else:
        raise HTTPException(status_code=404, detail=f"Resident does not exists!")


@router.delete("/{id}")
async def delete(id: UUID4, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    resident = db.query(ResidentProfile).filter(ResidentProfile.id == id, ResidentProfile.deleted_at == None).first()
    user = db.query(User).filter(User.email == current_user.email).first()
    # Ensure user is authenticated
    if not user:
        raise HTTPException(status_code=404, detail="Not authenticated")
    # Retrieve user id from the authenticated user
    userid = user.id

    if resident:
        resident.deleted_at = datetime.now()
        resident.deleted_by = userid
        db.commit()
        return {
            "message": f"Resident: {resident.id} deleted successfully!",
            "data": {
                   "deleted_at": resident.deleted_at,
                   "deleted_by": resident.deleted_by,
            }
        }
    else:
        raise HTTPException(status_code=404, detail=f"Resident does not exists!")





