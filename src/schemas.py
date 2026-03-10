from pydantic import BaseModel


class AQIInput(BaseModel):

    Country: str

    CO_AQI_Value: int
    Ozone_AQI_Value: int
    NO2_AQI_Value: int
    PM25_AQI_Value: int