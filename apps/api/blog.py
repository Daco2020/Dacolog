from fastapi import Request, APIRouter, status
from apps.service.logs import LogHandler, LogItem
from fastapi.responses import JSONResponse
from pymysql.err import IntegrityError


router = APIRouter(
    prefix="/users"
)


@router.get("/{user_id}/logs")
async def read_logs(request: Request, user_id: int):
    print(request)
    return {"message": f"{user_id}번 유저의 블로그를 준비중입니다."}


@router.post("/{user_id}/logs")
async def create_logs(request: Request, user_id: int, log_item: LogItem):
    try:
        content, category_id = log_item.content, log_item.category_id
        if LogHandler.insert([content, category_id]):
            result = {"message": "success" }
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    
    except IntegrityError: 
        result = {"message": "value error"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=result)
    
        