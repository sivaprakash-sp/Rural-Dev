from motor.motor_asyncio import AsyncIOMotorClient
import os

# Uses local MongoDB by default if no environment variable is provided
MONGO_DETAILS = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)

# Database Name
database = client.ruralfix_db

# Collections
users_collection = database.get_collection("users")
crops_collection = database.get_collection("crops")
complaints_collection = database.get_collection("complaints")

# Helper function to parse ObjectId to string for JSON serialization
def parse_db_object(item) -> dict:
    item["_id"] = str(item["_id"])
    return item
