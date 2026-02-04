from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.configs.config import config
from app.routes import health_api

app = FastAPI(title="AI Powered Blog Generation Service", version="1.0.0")

app.include_router(health_api.router)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

@app.middleware("http")
async def log_exceptions(request, call_next):
	try:
		response = await call_next(request)
		return response
	except Exception as e:
		return JSONResponse(
			status_code=e.status_code,
			content={"detail": e.description, "response": e.response}
		)

@app.get("/")
def read_root():
	return {"message": f"Welcome to the {config['application']['name']}!"}