# src/input_schema.py
from pydantic import BaseModel, Field


class AQIInput(BaseModel):
    Country: str = Field(..., alias="Country")
    CO_AQI_Value: int = Field(..., alias="CO AQI Value")
    CO_AQI_Category: str = Field(..., alias="CO AQI Category")
    Ozone_AQI_Value: int = Field(..., alias="Ozone AQI Value")
    Ozone_AQI_Category: str = Field(..., alias="Ozone AQI Category")
    NO2_AQI_Value: int = Field(..., alias="NO2 AQI Value")
    NO2_AQI_Category: str = Field(..., alias="NO2 AQI Category")
    PM25_AQI_Value: int = Field(..., alias="PM2.5 AQI Value")
    PM25_AQI_Category: str = Field(..., alias="PM2.5 AQI Category")

    class Config:
        allow_population_by_field_name = True