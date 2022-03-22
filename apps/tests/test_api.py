from unittest import TestCase
from fastapi import responses
from fastapi.testclient import TestClient
from apps.service.logs import LogHandler
from apps.service.users import AccountHandler
from apps.main import app
from .setup_mock_db import CreateMockData
from apps.api.account import create_account

client = TestClient(app)
mock_data = CreateMockData()


class TestBlog(TestCase):
    def setUp(self) -> None:
        super().setUp()
        mock_data.setup_categories()
        mock_data.setup_logs()

    def tearDown(self) -> None:
        mock_data.init_logs()
        mock_data.init_categories()
        
    def test_read_logs_all(self):
        response = client.get(f"/users/{1}/logs")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.text)

    def test_create_logs(self):
        id = mock_data.read_categories()['id']
        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
                "category_id": id
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"message": "success"})

        response = client.post(
            f"/users/{1}/logs",
            json={
                "content": "Test",
                "category_id": 0
            })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "value error"})
        
    def test_create_logs_unprocessable_entity(self):
        response = client.post(
            f"/users/{1}/logs",
            json={
            })
        self.assertEqual(response.status_code, 422)


class TestAccount(TestCase):
    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        mock_data.init_users()
        
    def test_singup_success(self):
        response = client.post("/account",
            json={
                "name": "test_name",
                "email" : "test@test.com",
                "password" : "1q2w3e4r"
            })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], "Create an account")

    def test_singup_failure(self):
        response = client.post("/account",
            json={
                "name": "test_name",
                "email" : "test",
                "password" : "1q2w3e4r"
            })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], "Email is invalid")

        response = client.post("/account",
            json={
                "name": "test_name",
                "email" : "test@test.com",
                "password" : "test"
            })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], "Password is invalid")

        client.post("/account",
            json={
                "name": "test_name",
                "email" : "test@test.com",
                "password" : "1q2w3e4r"
            })
        response = client.post("/account",
            json={
                "name": "test_name",
                "email" : "test@test.com",
                "password" : "1q2w3e4r"
            })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], "Email already exists")

    def test_login_success(self):
        self.test_singup_success()
        response = client.post("/account/login",
            json={
                "email" : "test@test.com",
                "password" : "1q2w3e4r"
            })

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['access_token'])
        
    def test_login_failure(self):
        response = client.post("/account/login",
            json={
                "email" : "test_failure@test.com",
                "password" : "1q2w3e4r"
            })

        self.assertEqual(response.status_code, 401)
        self.assertIsNotNone(response.json()['message'])
        
        response = client.post("/account/login",
            json={
                "email" : "test@test.com",
                "password" : "1q2w3e4r_failure"
            })

        self.assertEqual(response.status_code, 401)
        self.assertIsNotNone(response.json()['message'])