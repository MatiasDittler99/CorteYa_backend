def test_crud_cliente(client):
    # Crear cliente
    response = client.post("/clientes/", json={
        "nombre_completo": "Juan Pérez",
        "telefono": "123456789",
        "email": "juan@example.com"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre_completo"] == "Juan Pérez"
    cliente_id = data["id_cliente"]

    # Obtener cliente
    response = client.get(f"/clientes/{cliente_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "juan@example.com"

    # Actualizar cliente
    response = client.put(f"/clientes/{cliente_id}", json={
        "nombre_completo": "Juan Actualizado",
        "telefono": "123456789",
        "email": "juan@nuevo.com"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "juan@nuevo.com"

    # Eliminar cliente
    response = client.delete(f"/clientes/{cliente_id}")
    assert response.status_code == 200

    # Verificar que no existe más
    response = client.get(f"/clientes/{cliente_id}")
    assert response.status_code == 404
