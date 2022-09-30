from fastapi import FastAPI
app = FastAPI()

@app.get("/health", tags=["Health Check"])
async def root():
    return {"message": "Service is online."}
