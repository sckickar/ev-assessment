def test_create_address(client):
    response = client.post(
        "/addresses/",
        json={"name": "Central Park", "city": "New York",
              "latitude": 40.7812, "longitude": -73.9665}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Central Park"
    assert "id" in data


def test_create_address_invalid_coordinates(client):
    # Latitude must be between -90 and 90
    response = client.post(
        "/addresses/",
        json={"name": "Mars Base", "city": "Mars",
              "latitude": 150.0, "longitude": 0.0}
    )
    # Unprocessable Entity (Validation Error)
    assert response.status_code == 422


def test_get_address(client):
    # Create an address first
    post_response = client.post(
        "/addresses/",
        json={"name": "Office", "city": "London",
              "latitude": 51.5, "longitude": -0.1}
    )
    address_id = post_response.json()["id"]

    # Test: Retrieve it
    response = client.get(f"/addresses/{address_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Office"


def test_nearby_addresses(client):
    client.post(
        "/addresses/",
        json={"name": "Eiffel Tower", "city": "Paris",
              "latitude": 48.8584, "longitude": 2.2945}
    )

    client.post(
        "/addresses/",
        json={"name": "Tokyo Tower", "city": "Tokyo",
              "latitude": 35.6586, "longitude": 139.7454}
    )

    # Search within 50km of Paris
    response = client.get("/addresses/nearby?lat=48.85&lon=2.29&distance=50")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Eiffel Tower"


def test_delete_address(client):

    post_response = client.post(
        "/addresses/",
        json={"name": "Temp", "city": "Nowhere",
              "latitude": 0.0, "longitude": 0.0}
    )
    address_id = post_response.json()["id"]

    delete_response = client.delete(f"/addresses/{address_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/addresses/{address_id}")
    assert get_response.status_code == 404
