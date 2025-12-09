def test_get_users(session, config):
    url = f"{config['base_url']}/users?page=2"
    response = session.get(url)
    
    # Validación de código de estado
    assert response.status_code == 200

    data = response.json()
    
    # Validación de estructura
    assert "data" in data
    assert isinstance(data["data"], list)

    # Validación de contenido
    assert data["page"] == 2
