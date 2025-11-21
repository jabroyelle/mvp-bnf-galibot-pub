from fastapi import FastAPI, HTTPException
from model import DocumentReservationRequest, SeatReservationResponse, SeatReservationRequest
from datetime import date, timedelta
import json

with open('./data.json') as f:
  data = json.load(f)

app = FastAPI(title="Reservation APIs")

# --- Document Reservation ---

@app.get(
        "/documents/{document_id}/availability", 
        description="Check for document availability"
    )
def check_availability(document_id: str):
    if document_id not in data["documents"]:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "document_id": document_id, 
        "available_from": date.fromisoformat(data["documents"][document_id]["available_from"]),
        "isReserved":  data["documents"][document_id]["isReserved"]
    }

@app.post(
        "/documents{document_id}/reserve",
        description="Reserve a document"
    )
def reserve_document(request: DocumentReservationRequest):
    if request.document_id not in data["documents"]:
        raise HTTPException(status_code=404, detail="Document not found")
    if data["documents"][request.document_id]["isReserved"]:
        raise HTTPException(status_code=400, detail="Document not available on requested date")
    
    data["documents"][request.document_id]["isReserved"] = True
    data["documents"][request.document_id]["available_from"] = str(date.today() + timedelta(days=10))

    return {
        "message": "Reservation successful",
        "reservation": request.dict(),
        "available_from":  date.today() + timedelta(days=10)
    }

@app.delete(
        "/documents/{document_id}/reserve", 
        description="Check for document availability"
    )
def check_availability(document_id: str):
    if document_id not in data["documents"]:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "document_id": document_id, 
        "available_from": date.today(),
        "isReserved": False
    }

# --- Exhibition Reservation ---

@app.get(
        "/exhibition/{exhibit_id}", 
        response_model=SeatReservationResponse,
        description="Check if an exhibition is sold out"
    )
def get_available_seats(exhibit_id: str):
    if exhibit_id in data["available_seats"]:
        return SeatReservationResponse(
            message="Current available seats",
            remaining_seats=data["available_seats"][exhibit_id]
        )
    else :
        raise HTTPException(status_code=404, detail="This exhibit does not exist")

@app.post(
        "/exhibition/{exhibit_id}/reserve", 
        response_model=SeatReservationResponse,
        description="Reserve a place for an exhibition"
    )
def reserve_seats(request: SeatReservationRequest, exhibit_id: str):
    if request.seats > data["available_seats"][exhibit_id]:
        raise HTTPException(status_code=400, detail="The event is sold out")
    
    data["available_seats"][exhibit_id] -= request.seats
    
    return SeatReservationResponse(
        message=f"{request.seats} ticket reserved for {request.name}",
        remaining_seats=data["available_seats"][exhibit_id]
    )

# --- Exhibition Reservation ---

@app.get(
        "/pass/{pass_id}", 
        response_model=SeatReservationResponse,
        description="Check if an exhibition is sold out"
    )
def get_available_seats(pass_id: str):
    if pass_id in data["available_seats"]:
        return SeatReservationResponse(
            message="Current available seats",
            remaining_seats=data["available_seats"][pass_id]
        )
    else :
        raise HTTPException(status_code=404, detail="This exhibit does not exist")

@app.post(
        "/exhibition/{exhibit_id}/reserve", 
        response_model=SeatReservationResponse,
        description="Reserve a place for an exhibition"
    )
def reserve_seats(request: SeatReservationRequest, exhibit_id: str):
    if request.seats > data["available_seats"][exhibit_id]:
        raise HTTPException(status_code=400, detail="The event is sold out")
    
    data["available_seats"][exhibit_id] -= request.seats
    
    return SeatReservationResponse(
        message=f"{request.seats} ticket reserved for {request.name}",
        remaining_seats=data["available_seats"][exhibit_id]
    )
