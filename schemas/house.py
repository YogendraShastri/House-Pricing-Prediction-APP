from pydantic import BaseModel, Field, field_validator
from typing import List


class HouseFeatures(BaseModel):
    area: float = Field(..., examples=[1000])
    bedrooms: int = Field(..., examples=[3], ge=0)
    bathrooms: int = Field(..., examples=[2], ge=0)
    stories: int = Field(..., examples=[1], ge=0)
    parking: int = Field(..., examples=[1], ge=0)
    mainroad: str = Field(..., examples=["yes"])
    guestroom: str = Field(..., examples=["no"])
    basement: str = Field(..., examples=["no"])
    hotwaterheating: str = Field(..., examples=["no"])
    airconditioning: str = Field(..., examples=["yes"])
    prefarea: str = Field(..., examples=["no"])
    furnishingstatus: str = Field(..., examples=["semi-furnished"])

    @field_validator("mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", mode="before")
    @classmethod
    def yes_no_validator(cls, v: str) -> str:
        if v.lower() not in {"yes", "no"}:
            raise ValueError("must be yes/no")
        return v.lower()

    @field_validator("furnishingstatus", mode="before")
    @classmethod
    def furnishing_validator(cls, v: str) -> str:
        v_lower = v.lower()
        if v_lower not in {"furnished", "semi-furnished", "unfurnished"}:
            raise ValueError("furnishingstatus must be one of: furnished, semi-furnished, unfurnished")
        return v_lower

class BatchRequest(BaseModel):
    items: List[HouseFeatures]