from fastapi import Request, APIRouter, status
from apps.service.logs import LogHandler, LogItem
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pymysql.err import IntegrityError


router = APIRouter(
    prefix="/users"
)


@router.get("/")
async def read_users(request: Request, category: int = 0, offset: int = 0, limit: int = 10):
    pass


@router.get("/{user_id}/logs")
async def read_logs(request: Request, user_id: int):
    result = {"message": jsonable_encoder(LogHandler.select_all())}
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@router.post("/{user_id}/logs")
async def create_logs(request: Request, user_id: int, log_item: LogItem):
    try:
        LogHandler.insert([log_item.content, log_item.category_id])
        result = {"message": "success"}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    
    except IntegrityError: 
        result = {"message": "value error"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=result)
    
        