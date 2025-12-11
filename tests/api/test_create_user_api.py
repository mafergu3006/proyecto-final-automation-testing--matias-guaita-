from utils.api_client import APIClient

def test_create_user_success():
    client = APIClient()

    response = client.create_user(name="Mario", job="QA Tester")

    assert response.status_code == 201

    json_body = response.json()

    assert json_body["name"] == "Mario"
    assert json_body["job"] == "QA Tester"
    assert "id" in json_body
    assert "createdAt" in json_body
