from sqlalchemy import DateTime, ForeignKey, func, Enum, String
from src.database import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from datetime import datetime
from typing import Optional

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    email:Mapped[str] = mapped_column(unique=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
