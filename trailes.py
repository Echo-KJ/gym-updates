
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DB_FILE = "gym.db"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def setup_database():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            goal TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


# Create the database table when the app starts.
setup_database()


class Lead(BaseModel):
    name: str
    email: str
    goal: str


def check_lead(lead: Lead):
    if not lead.name.strip():
        return "Name is required"

    if "@" not in lead.email or "." not in lead.email:
        return "Email is not valid"

    if not lead.goal.strip():
        return "Goal is required"

    if len(lead.name) > 100 or len(lead.goal) > 300:
        return "Input is too long"

    return None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/leads")
def create_lead(lead: Lead):
    problem = check_lead(lead)

    if problem is not None:
        raise HTTPException(status_code=400, detail=problem)

    conn = get_connection()

    try:
        conn.execute(
            "INSERT INTO leads (name, email, goal) VALUES (?, ?, ?)",
            (
                lead.name.strip(),
                lead.email.strip(),
                lead.goal.strip(),
            ),
        )
        conn.commit()
    finally:
        conn.close()

    return {"success": True, "message": "Enquiry saved"}


@app.get("/leads")
def list_leads():
    conn = get_connection()

    try:
        rows = conn.execute(
            """
            SELECT id, name, email, goal, created_at
            FROM leads
            ORDER BY id DESC
            """
        ).fetchall()

        return [dict(row) for row in rows]
    finally:
        conn.close()
