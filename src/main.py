"""Главный файл приложения UniMarket"""
from fastapi import FastAPI
from src.config import settings

app = FastAPI(
	title=settings.PROJECT_NAME,
	version=settings.VERSION,
	description="Платформа для покупки и продажи товаров между студентами",
	docs_url="/docs",
	redoc_url="/redoc",
)

@app.get("/")
async def root():
	"""Корневой endpoint - приветствие"""
	return {"message": "Добро пожаловать в UniMarket!", "version": settings.VERSION}

@app.get("/health")
async def health_check():
	"""Health check endpoint - проверка работоспособности"""
	return {"status": "healthy", "project": settings.PROJECT_NAME}

@app.get("/about")
async def about():
	return {
		"project": settings.PROJECT_NAME,
		"description": "Студенческий маркетплейс",
		"author": settings.AUTHOR,
	}

if __name__ == "__main__":
	import uvicorn
	uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
