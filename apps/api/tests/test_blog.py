from fastapi.testclient import TestClient
from apps.main import app

client = TestClient(app)

    
def test_create_logs():
    response = client.post(
        f"/users/{1}/logs",
        json={
            "content": "string",
            "category_id": 1
        })
    assert response.status_code == 201
    assert response.json() == {"message": "success"}

def test_create_logs_string_category_id():
    response = client.post(
        f"/users/{1}/logs",
        json={
            "content": "test",
            "category_id": "1"
        })
    assert response.status_code == 201
    assert response.json() == {"message": "success"}

def test_create_logs_invaild_category_id():
    response = client.post(
        f"/users/{1}/logs",
        json={
            "content": "string",
            "category_id": -1
        })
    assert response.status_code == 400
    assert response.json() == {"message": "value error"}
    
def test_create_logs_unprocessable_entity():
    response = client.post(
        f"/users/{1}/logs",
        json={
            "content": "string",
        })
    assert response.status_code == 422
    
