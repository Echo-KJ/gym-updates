
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary storage in memory
leads = []


# Define the structure of an enquiry
class Lead(BaseModel):
    name: str
    email: str
    goal: str


# Validate the enquiry
def check_lead(lead: Lead):
    if lead.name.strip() == "":
        return "Name is required"

    if "@" not in lead.email or "." not in lead.email:
        return "Email is not valid"

    if lead.goal.strip() == "":
        return "Goal is required"

    if len(lead.name) > 100 or len(lead.goal) > 300:
        return "Input is too long"

    return None


# Check whether the backend is running
@app.get("/health")
def health():
    return {"status": "ok"}


# Receive a new enquiry
@app.post("/leads")
def create_lead(lead: Lead):
    problem = check_lead(lead)

    if problem is not None:
        raise HTTPException(status_code=400, detail=problem)

    leads.append(lead.model_dump())

    print("New enquiry:", lead)

    return {
        "success": True,
        "message": "Enquiry received"
    }
