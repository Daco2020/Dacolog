from unittest import TestCase
from fastapi.testclient import TestClient
from apps.service.logs import LogHandler
from apps.main import app

client = TestClient(app)


class TestBlog(TestCase):
    def setUp(self) -> None:
        super().setUp()
        LogHandler.insert(['Test', 1])

    def tearDown(self) -> None:
        LogHandler.delete(['Test'])
        
        
    # test_read_logs
    def test_read_logs_all(self):
        response = client.get(f"/users/{1}/logs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bool(response.text), True)


    # test_create_logs
    def test_create_logs(self):
        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
                "category_id": 1
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "success"})

    def test_create_logs_string_category_id(self):
        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
                "category_id": "1"
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "success"})

    def test_create_logs_invalid_category_id(self):
        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
                "category_id": -1
            })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "value error"})
        
    def test_create_logs_unprocessable_entity(self):
        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
            })
        self.assertEqual(response.status_code, 422)