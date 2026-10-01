from pydantic import BaseModel, Field
from typing import Optional

class AddressBase(BaseModel):
    name: str = Field(json_schema_extra={"example" : "Home"})
    street: Optional[str] = Field(None, json_schema_extra={"example": "123 Street"})
    city: str = Field(json_schema_extra={"example" : "Metropolis"})
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude between -90 and 90")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude between -180 and 180")

class AddressCreate(AddressBase):
    pass

class AddressUpdate(BaseModel):
    name: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = Field(None, ge=-90.0, le=90.0)
    longitude: Optional[float] = Field(None, ge=-180.0, le=180.0)

class AddressResponse(AddressBase):
    id: int
    # Allows Pydantic to read ORM models
    model_config = {"from_attributes": True} 