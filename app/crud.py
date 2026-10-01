import logging
from sqlalchemy.orm import Session
from app.models import Address
from app.schemas import AddressCreate, AddressUpdate
from app.utils import calculate_haversine_distance

logger = logging.getLogger(__name__)


def create_address(db: Session, address: AddressCreate) -> Address:
    db_address = Address(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    logger.info(f"Address created with ID: {db_address.id}")
    return db_address


def get_address_by_id(db: Session, address_id: int) -> Address:
    return db.query(Address).filter(Address.id == address_id).first()


def update_address(db: Session, db_address: Address, updates: AddressUpdate) -> Address:
    update_data = updates.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    logger.info(f"Address updated with ID: {db_address.id}")
    return db_address


def delete_address(db: Session, db_address: Address):
    db.delete(db_address)
    db.commit()
    logger.info(f"Address deleted with ID: {db_address.id}")


def get_addresses_within_radius(db: Session, lat: float, lon: float, radius_km: float):
    all_addresses = db.query(Address).all()
    nearby_addresses = []

    for addr in all_addresses:
        distance = calculate_haversine_distance(
            lat, lon, addr.latitude, addr.longitude)
        if distance <= radius_km:
            nearby_addresses.append(addr)

    return nearby_addresses
