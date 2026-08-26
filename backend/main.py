from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI App
app = FastAPI(title="RuralFix - Agro MedKnow Nexus API")

# Configure CORS so the frontend can connect
# Since it's a hackathon project, we allow all origins for now
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic Health Check Route
@app.get("/api/health")
async def health_check():
    return {"status": "success", "message": "Backend is running and connected!"}

# Import routers here in the future
# app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
# app.include_router(crops_router, prefix="/api/crops", tags=["crops"])
# app.include_router(complaints_router, prefix="/api/complaints", tags=["complaints"])

if __name__ == "__main__":
    import uvicorn
    # This runs the server on http://localhost:8080
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
