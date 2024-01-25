from sqlalchemy.orm import relationship

from config.database import Base
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

import uuid


class BarangayOfficial(Base):
    __tablename__ = "barangayofficials"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=False)
    suffix = Column(String(50), nullable=True)
    birthday = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    contact_no = Column(String(50), nullable=True)
    position = Column(String(50), nullable=True)
    start_term = Column(String(50), nullable=True)
    end_term = Column(String(50), nullable=True)
    photo_path = Column(String(50), nullable=True)
    # resident_id = Column(UUID(as_uuid=True), ForeignKey("residentprofiles.id"), nullable=False)

    # Mandatory columns
    created_at = Column(DateTime, nullable=False)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_at = Column(DateTime, nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    deleted_by = Column(UUID(as_uuid=True), nullable=True)

    # Relationship
    # barangay_official_ordinance = relationship("Ordinance", back_populates="ordinance_barangay_official")
