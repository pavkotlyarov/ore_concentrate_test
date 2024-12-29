from datetime import date
from pydantic import BaseModel

class Concentrate(BaseModel):
    name: str
    iron_content: float
    silicon_content: float
    aluminium_content: float
    calcium_content: float
    sulfur_content: float
    date: date

class BulkConcentrate(BaseModel):
    data: list[Concentrate]


class ContentReport(BaseModel):
    minimum: float
    maximum: float
    average: float

class Report(BaseModel):
    iron_content: ContentReport
    silicon_content: ContentReport
    aluminium_content: ContentReport
    calcium_content: ContentReport
    sulfur_content: ContentReport
