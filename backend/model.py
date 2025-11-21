from pydantic import BaseModel
from datetime import date

class DocumentReservationRequest(BaseModel):
    document_id: str
    # reservation_date: date

class SeatReservationRequest(BaseModel):
    name: str
    seats: int

class SeatReservationResponse(BaseModel):
    message: str
    remaining_seats: int