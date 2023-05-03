from fastapi.testclient import TestClient

from ....app.backend.main import app

client = TestClient(app)


# def test_post_play_one():
#     test_cases = [
#         {
#             "json_body": {"message": "Hello World"},
#             "expected_status_code": 401,
#             "expected_response": {
#                 "detail": "No credentials provided, either username and password or token must be set"
#             },
#         },
#         {
#             "json_body": {
#                 "message": "Hello World",
#                 "auth": {"token": "token"},
#             },
#             "expected_status_code": 200,
#             "expected_response": {"message": "Hello World", "logged_in": True},
#         },
#     ]

#     for test_case in test_cases:
#         response = client.post(
#             "/play/one",
#             json=test_case["json_body"],
#         )
#         assert response.status_code == test_case["expected_status_code"]
#         assert response.json() == test_case["expected_response"]


def test_post_play_one():
    test_cases = [
        {
            "json_body": {
                "play": {"message": "my message"},
                "auth": {"token": "token"},
            },
            "expected_status_code": 200,
            "expected_response": {
                "message": "my message",
                "logged_in": True,
            },
        },
        {
            "json_body": {
                "play": {"message": "my message"},
                "auth": {"username": "user", "password": "pass"},
            },
            "expected_status_code": 200,
            "expected_response": {
                "message": "my message",
                "logged_in": True,
            },
        },
    ]

    for test_case in test_cases:
        response = client.post(
            "/play/one",
            json=test_case["json_body"],
        )
        assert response.status_code == test_case["expected_status_code"]
        assert response.json() == test_case["expected_response"]
