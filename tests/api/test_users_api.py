from utils.api_client import APIClient

def test_get_users_success():
    client = APIClient()
    
    response = client.get_users(page=2)

    assert response.status_code == 200

    json_body = response.json()

    assert "data" in json_body
    assert isinstance(json_body["data"], list)
    assert len(json_body["data"]) > 0

    # Validar estructura
    for user in json_body["data"]:
        assert "id" in user
        assert "email" in user
