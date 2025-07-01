def test_empleado_especialidad(client):
    # Crear dependencias
    emp = client.post("/empleados/", json={"nombre_completo": "Relación Empleado"}).json()
    esp = client.post("/especialidades/", json={"nombre_completo": "Peinado"}).json()

    # Crear relación
    response = client.post("/empleado-especialidades/", json={
        "id_empleado": emp["id_empleado"],
        "id_especialidad": esp["id_especialidad"]
    })
    assert response.status_code == 200

    # Listar
    res = client.get("/empleado-especialidades/")
    assert res.status_code == 200
    assert any(r["id_empleado"] == emp["id_empleado"] for r in res.json())

    # Eliminar relación
    res = client.delete(f"/empleado-especialidades/?id_empleado={emp['id_empleado']}&id_especialidad={esp['id_especialidad']}")
    assert res.status_code == 200
