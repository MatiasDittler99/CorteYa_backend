def test_crud_especialidad(client):
    response = client.post("/especialidades/", json={"nombre_completo": "Color"})
    assert response.status_code == 200
    id_esp = response.json()["id_especialidad"]

    # Get
    res = client.get(f"/especialidades/{id_esp}")
    assert res.status_code == 200

    # Put
    res = client.put(f"/especialidades/{id_esp}", json={"nombre_completo": "Corte"})
    assert res.status_code == 200

    # Delete
    res = client.delete(f"/especialidades/{id_esp}")
    assert res.status_code == 200
