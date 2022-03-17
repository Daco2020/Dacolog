from fastapi import Request
from apps.model.logs import LogHandler, LogItem
from fastapi import APIRouter


router = APIRouter(
    prefix="/users"
)


@router.get("/{user_id}/logs")
async def read_logs(request: Request, user_id: int):
    print(request)
    return {"message": f"{user_id}번 유저의 블로그를 준비중입니다."}


@router.post("/{user_id}/logs")
async def create_logs(request: Request, user_id: int, log_item: LogItem):
    content, category_id = log_item.content, log_item.category_id
    result = LogHandler.insert([content, category_id])
    return {"message": result}