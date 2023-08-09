import uvicorn
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, docs_url='/api/docs', redoc_url=None)


if __name__ == "__main__":
    uvicorn.run(app)