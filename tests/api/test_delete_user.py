def test_delete_user(session, config):
    # ReqRes no guarda usuarios realmente, pero DELETE devuelve 204
    user_id = 2
    url = f"{config['base_url']}/users/{user_id}"

    response = session.delete(url)

    # Validación de código de estado
    assert response.status_code == 204
