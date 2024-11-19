from pydantic import BaseModel


class PropertySchema(BaseModel):
    name: str
    address: str
    rent: float
    is_available: bool = True

    class Config:
        orm_mode = True


class UpdatePropertySchema(BaseModel):
    name: str | None = None
    address: str | None = None
    rent: float | None = None
    is_available: bool | None = None

    class Config:
        orm_mode = True
