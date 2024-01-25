from fastapi import FastAPI, APIRouter

from test.api.endpoints import router as api_router


router = APIRouter(
    prefix='/api'
)


app = FastAPI(title='Симуляция логистической системы')
app.include_router(api_router)
