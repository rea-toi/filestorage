from src.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional, List
from datetime import datetime
from sqlalchemy import String, UUID, Enum, Integer, Float, DateTime, ForeignKey
from uuid import UUID, uuid4


class Files(Base):
    __tablename__ = "files"
    file_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    current_version_id: Mapped[UUID] = mapped_column(ForeignKey("file_versions.id"), nullable=True)

    current_version: Mapped["FileVersion"] = relationship("FileVersion", foreign_keys=[current_version_id], post_update=True)
    versions: Mapped[List["FileVersion"]] = relationship(back_populates="file")


class FileVersion(Base):
    __tablename__ = "file_versions"
    file_id: Mapped[UUID] = mapped_column(ForeignKey("files.id"))
    file_path: Mapped[str] = mapped_column(String)
    version_number: Mapped[int] = mapped_column(Integer)
    file_hash: Mapped[str] = mapped_column(String, nullable=True)

    file: Mapped["Files"] = relationship(back_populates="versions")