"""
MolGen-Lab Backend

Folder Structure:
- backend/: Core logic and API endpoints.
- backend/models/: Database models and data schemas.
- backend/utils/: Helper functions and utilities.
- backend/db/: Database connection and session management.

- frontend/: React/Vite/Next.js files (placeholder).

- notebooks/: Jupyter notebooks for research and analysis.
- data/: Raw and processed data files (e.g., JSON, CSV).
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MolGen-Lab API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
