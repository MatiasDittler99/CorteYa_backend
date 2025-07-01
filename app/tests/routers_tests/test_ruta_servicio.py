def test_crud_servicio(client):
    response = client.post("/servicios/", json={
        "nombre_servicio": "Barba",
        "duracion": 30,
        "precio": 1500.0
    })
    assert response.status_code == 200
    id_servicio = response.json()["id_servicio"]

    res = client.get(f"/servicios/{id_servicio}")
    assert res.status_code == 200

    res = client.put(f"/servicios/{id_servicio}", json={
        "nombre_servicio": "Barba Deluxe",
        "duracion": 40,
        "precio": 1800.0
    })
    assert res.status_code == 200

    res = client.delete(f"/servicios/{id_servicio}")
    assert res.status_code == 200
