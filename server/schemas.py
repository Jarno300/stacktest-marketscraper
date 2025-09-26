from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Literal


PlatformLiteral = Literal["vinted", "2dehands", "facebook"]


class ListingBase(BaseModel):
    platform: PlatformLiteral
    title: str
    description: str
    price_cents: int
    delivery_cost_cents: Optional[int] = None
    postal_code: Optional[str] = None
    city: Optional[str] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    url: str
    images: List[str] = Field(default_factory=list)
    uploaded_at: datetime


class ListingOut(ListingBase):
    id: int
    distance_km: Optional[float] = None # computed when radius filter used


class Config:
    from_attributes = True


class ListingsResponse(BaseModel):
    total: int
    items: list[ListingOut]