from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Concentrate(Base):
    __tablename__ = 'concentrate'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    iron_content: Mapped[float] = mapped_column(nullable=False)
    silicon_content: Mapped[float] = mapped_column(nullable=False)
    aluminium_content: Mapped[float] = mapped_column(nullable=False)
    calcium_content: Mapped[float] = mapped_column(nullable=False)
    sulfur_content: Mapped[float] = mapped_column(nullable=False)

    date: Mapped[datetime] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
