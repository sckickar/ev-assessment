from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app import crud
from app.schemas import AddressCreate, AddressUpdate, AddressResponse
from app.database import get_db

router = APIRouter(prefix="/addresses", tags=["Addresses"])


@router.post("/", response_model=AddressResponse, status_code=201)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)


@router.get("/nearby", response_model=List[AddressResponse])
def get_nearby_addresses(
    latitude: float = Query(..., alias="lat", ge=-90.0, le=90.0,
                            description="Target latitude"),
    longitude: float = Query(..., alias="lon", ge=-180.0, le=180.0,
                             description="Target longitude"),
    radius_km: float = Query(..., alias="distance", gt=0,
                             description="Search radius in kilometers"),
    db: Session = Depends(get_db)
):
    return crud.get_addresses_within_radius(db, lat=latitude, lon=longitude, radius_km=radius_km)


@router.get("/{address_id}", response_model=AddressResponse)
def get_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address_by_id(db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@router.put("/{address_id}", response_model=AddressResponse)
def update_address(address_id: int, address_update: AddressUpdate, db: Session = Depends(get_db)):
    db_address = crud.get_address_by_id(db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return crud.update_address(db=db, db_address=db_address, updates=address_update)


@router.delete("/{address_id}", status_code=204)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address_by_id(db, address_id=address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    crud.delete_address(db=db, db_address=db_address)
    return None
