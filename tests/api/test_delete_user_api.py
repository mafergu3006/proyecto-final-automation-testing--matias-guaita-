from utils.api_client import APIClient

def test_delete_user():
    client = APIClient()

    response = client.delete_user(2)


    assert response.status_code == 204
    assert response.text == ''
