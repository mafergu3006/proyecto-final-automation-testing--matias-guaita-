def test_create_user(session, config):
    url = f"{config['base_url']}/users"
    payload = {
        "name": "John Doe",
        "job": "Software Engineer"
    }

    response = session.post(url, json=payload)

    # Validación de código de estado
    assert response.status_code == 201

    data = response.json()

    # Validación de contenido
    assert data["name"] == "John Doe"
    assert data["job"] == "Software Engineer"
    assert "id" in data
    assert "createdAt" in data
