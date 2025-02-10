from fastapi import FastAPI
from app.routers import books  # Ensure the import is correct
from fastapi.middleware.cors import CORSMiddleware  # Import this
app = FastAPI()

# Allow CORS for the frontend at http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if your frontend URL changes
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the books router for all API endpoints
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Inventory API"}
