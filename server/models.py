from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, Enum, UniqueConstraint, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from .database import Base
import enum

class Platform(str, enum.Enum):
    vinted = "vinted"
    t2h = "2dehands"
    fb = "facebook"

class PostalCode(Base):
    __tablename__ = "postal_codes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    city: Mapped[str] = mapped_column(String(120))
    lat: Mapped[float] = mapped_column(Numeric(9,6)) # 48.123456
    lon: Mapped[float] = mapped_column(Numeric(9,6))
    __table_args__ = (UniqueConstraint('code', 'city', name='uq_postal_code_city'),)

class Listing(Base):
    __tablename__ = "listings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    platform: Mapped[str] = mapped_column(Enum(Platform), index=True)
    title: Mapped[str] = mapped_column(String(300), index=True)
    description: Mapped[str] = mapped_column(Text)
    price_cents: Mapped[int] = mapped_column(Integer, index=True)
    # For Vinted: store delivery cost cents instead of geo; for others, prefer geo.
    delivery_cost_cents: Mapped[int | None] = mapped_column(Integer, nullable=True)


    # Location
    postal_code: Mapped[str | None] = mapped_column(String(10), index=True)
    city: Mapped[str | None] = mapped_column(String(120))
    lat: Mapped[float | None] = mapped_column(Numeric(9,6))
    lon: Mapped[float | None] = mapped_column(Numeric(9,6))


    # Other
    url: Mapped[str] = mapped_column(String(1000), unique=True, index=True)
    images: Mapped[list] = mapped_column(JSON, default=list) # list of image URLs
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, index=True, default=datetime.utcnow)


    __table_args__ = (
    UniqueConstraint("url", name="uq_listing_url"),
)