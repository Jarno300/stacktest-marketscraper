from fastapi import Query
from typing import Optional


class ListingFilters:
    def __init__(
    self,
    q: Optional[str] = Query(None, description="Search in title/description"),
    platform: Optional[str] = Query(None, regex="^(vinted|2dehands|facebook)$"),
    min_price: Optional[int] = Query(None, ge=0, description="Min price (cents)"),
    max_price: Optional[int] = Query(None, ge=0, description="Max price (cents)"),
    uploaded_after: Optional[str] = Query(None, description="ISO timestamp"),
    postal_code: Optional[str] = Query(None, description="Belgian postal code to center distance"),
    max_km: Optional[float] = Query(None, ge=0, description="Max distance in km"),
    limit: int = Query(24, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
        self.q = q
        self.platform = platform
        self.min_price = min_price
        self.max_price = max_price
        self.uploaded_after = uploaded_after
        self.postal_code = postal_code
        self.max_km = max_km
        self.limit = limit
        self.offset = offset