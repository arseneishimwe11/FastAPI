from sqlalchemy.orm import Session
from app.models.property_model import Property
from app.schemas.property_schema import PropertySchema


def get_properties(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Property).offset(skip).limit(limit).all()


def get_property_by_id(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()


def create_property(db: Session, property: PropertySchema):
    new_property = Property(
        name=property.name,
        address=property.address,
        rent=property.rent,
        is_available=property.is_available,
    )
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property


def update_property(db: Session, property_id: int, updated_data: dict):
    property_to_update = get_property_by_id(db, property_id)
    if not property_to_update:
        return None

    for key, value in updated_data.items():
        setattr(property_to_update, key, value)

    db.commit()
    db.refresh(property_to_update)
    return property_to_update


def delete_property(db: Session, property_id: int):
    property_to_delete = get_property_by_id(db, property_id)
    if property_to_delete:
        db.delete(property_to_delete)
        db.commit()
        return True
    return False
