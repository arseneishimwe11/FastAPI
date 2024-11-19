from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.config import SessionLocal
from app.schemas.property_schema import PropertySchema, UpdatePropertySchema
from app.crud.property_crud import (
    get_properties,
    get_property_by_id,
    create_property,
    update_property,
    delete_property,
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/properties", tags=["Properties"])
def list_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_properties(db, skip, limit)


@router.get("/properties/{property_id}", tags=["Properties"])
def retrieve_property(property_id: int, db: Session = Depends(get_db)):
    property = get_property_by_id(db, property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property


@router.post("/properties", tags=["Properties"])
def add_property(property: PropertySchema, db: Session = Depends(get_db)):
    return create_property(db, property)


@router.put("/properties/{property_id}", tags=["Properties"])
def modify_property(property_id: int, property: UpdatePropertySchema, db: Session = Depends(get_db)):
    updated_property = update_property(db, property_id, property.dict(exclude_unset=True))
    if not updated_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return updated_property


@router.delete("/properties/{property_id}", tags=["Properties"])
def remove_property(property_id: int, db: Session = Depends(get_db)):
    if not delete_property(db, property_id):
        raise HTTPException(status_code=404, detail="Property not found")
    return {"detail": "Property deleted"}
