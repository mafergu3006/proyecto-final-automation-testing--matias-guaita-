def test_create_and_get_user(session, config):
    # Crear usuario
    create_payload = {"name": "Alice", "job": "Tester"}
    create_resp = session.post(f"{config['base_url']}/users", json=create_payload)
    assert create_resp.status_code == 201

    user_id = create_resp.json().get("id")
    assert user_id is not None

    # Intentar obtener usuario (ReqRes es dummy, aquí solo validamos el flujo)
    get_resp = session.get(f"{config['base_url']}/users/{user_id}")
    
    # Como ReqRes no guarda realmente, se espera 404
    assert get_resp.status_code == 404
