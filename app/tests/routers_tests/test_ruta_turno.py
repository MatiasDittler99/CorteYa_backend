from datetime import date, time

def test_crud_turno(client):
    cliente = client.post("/clientes/", json={
        "nombre_completo": "Cliente Turno",
        "telefono": "111",
        "email": "turno@example.com"
    }).json()
    empleado = client.post("/empleados/", json={"nombre_completo": "Empleado Turno"}).json()
    servicio = client.post("/servicios/", json={
        "nombre_servicio": "Corte",
        "duracion": 30,
        "precio": 1000.0
    }).json()

    # Crear turno
    response = client.post("/turnos/", json={
        "id_cliente": cliente["id_cliente"],
        "id_empleado": empleado["id_empleado"],
        "id_servicio": servicio["id_servicio"],
        "fecha": str(date.today()),
        "hora": "10:00",
        "estado": "pendiente"
    })
    assert response.status_code == 200
    id_turno = response.json()["id_turno"]

    # Get
    res = client.get(f"/turnos/{id_turno}")
    assert res.status_code == 200

    # Delete
    res = client.delete(f"/turnos/{id_turno}")
    assert res.status_code == 200
