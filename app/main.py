import logging
from fastapi import FastAPI
from app.database import engine, Base

from app.routers import addresses

# Centralized Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)
logger.info("Database initialized successfully.")

# Instantiate FastAPI
app = FastAPI(
    title="Address Book API",
    description="A modular FastAPI app to manage addresses and find nearby locations.",
    version="1.0.0"
)

app.include_router(addresses.router)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Welcome to the Address Book API"}