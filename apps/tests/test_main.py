from fastapi.testclient import TestClient
from apps.main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Daco!"}
    
def test_get_users_user_id_logs_list():
    response = client.get("/users/1/logs")
    assert response.status_code == 200
    assert response.json() == {"message": "1번 유저의 블로그를 준비중입니다."}

def test_get_users_user_id_logs_list():
    response = client.get("/users/1/logs")
    assert response.status_code == 200
    assert response.json() == {"message": "1번 유저의 블로그를 준비중입니다."}

