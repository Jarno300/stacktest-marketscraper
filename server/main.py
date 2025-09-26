from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select, and_, or_, func
from sqlalchemy.orm import Session
from datetime import datetime
from server.database import Base, engine, get_db
from server.models import Listing, PostalCode
from server.schemas import ListingsResponse, ListingOut
from server.deps import ListingFilters
from server.utils_distance import haversine_km

app = FastAPI(title="MarketScraper API", version="1.0.0")
Base.metadata.create_all(bind=engine)

app.get("/health")
def health():
    return {"status": "ok"}