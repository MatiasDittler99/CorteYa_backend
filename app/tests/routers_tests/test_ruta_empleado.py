def test_crud_empleado(client):
    response = client.post("/empleados/", json={"nombre_completo": "Empleado 1"})
    assert response.status_code == 200
    data = response.json()
    assert data["nombre_completo"] == "Empleado 1"
    id_empleado = data["id_empleado"]

    # Get
    res = client.get(f"/empleados/{id_empleado}")
    assert res.status_code == 200

    # Put
    res = client.put(f"/empleados/{id_empleado}", json={"nombre_completo": "Actualizado"})
    assert res.status_code == 200
    assert res.json()["nombre_completo"] == "Actualizado"

    # Delete
    res = client.delete(f"/empleados/{id_empleado}")
    assert res.status_code == 200
