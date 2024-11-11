"""
    "/api/v1/clients" GETx, POSTx
    "/api/v1/clients/{id} GETx PUTx DELETEx"
    "/api/v1/clients/{id}/orders" GETx

    TODO: Test order creation, update, and deletion for a client
"""
import requests
import pytest

BASE_URL = "http://localhost:3000"
API_KEY = "a1b2c3d4e5"

@pytest.mark.run(order=1)
def test_get_clients():
    response = requests.get(BASE_URL + "/api/v1/clients", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=2)
def test_create_client():
    body = {
        "id": 1,
        "name": "John Doe",
        "address": "123 Main St",
        "city": "Springfield",
        "zip_code": "12345",
        "province": "IL",
        "country": "USA",
        "contact_name": "Jane Doe",
        "contact_phone": "123-456-7890",
        "contact_email": "test@example.com"
    }
    response = requests.post(BASE_URL + "/api/v1/clients", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 201

@pytest.mark.run(order=3)
def test_get_clients():
    response = requests.get(BASE_URL + "/api/v1/clients", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    clients = response.json()
    assert len(clients) == 1

@pytest.mark.run(order=4)
def test_get_client():
    response = requests.get(BASE_URL + "/api/v1/clients/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    client = response.json()
    assert client["id"] == 1
    assert client["name"] == "John Doe"
    assert client["address"] == "123 Main St"
    assert client["city"] == "Springfield"
    assert client["zip_code"] == "12345"
    assert client["province"] == "IL"
    assert client["country"] == "USA"
    assert client["contact_name"] == "Jane Doe"
    assert client["contact_phone"] == "123-456-7890"
    assert client["contact_email"] == "test@example.com"

@pytest.mark.run(order=5)
def test_update_client():
    body = {
        "name": "Jane Doe",
        "address": "456 Elm St",
        "city": "Springfield",
        "zip_code": "12345",
        "province": "IL",
        "country": "USA",
        "contact_name": "John Doe",
        "contact_phone": "123-456-7890",
        "contact_email": "john@doe.com"
    }
    response = requests.put(BASE_URL + "/api/v1/clients/1", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 200

@pytest.mark.run(order=6)
def test_get_client():
    response = requests.get(BASE_URL + "/api/v1/clients/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    client = response.json()
    assert client["id"] == 1
    assert client["name"] == "Jane Doe"
    assert client["address"] == "456 Elm St"
    assert client["city"] == "Springfield"
    assert client["zip_code"] == "12345"
    assert client["province"] == "IL"
    assert client["country"] == "USA"
    assert client["contact_name"] == "John Doe"
    assert client["contact_phone"] == "123-456-7890"
    assert client["contact_email"] == "john@doe.com"

@pytest.mark.run(order=7)
def test_get_client_orders():
    response = requests.get(BASE_URL + "/api/v1/clients/1/orders", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=8)
def test_delete_client():
    response = requests.delete(BASE_URL + "/api/v1/clients/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 204

@pytest.mark.run(order=9)
def test_get_clients():
    response = requests.get(BASE_URL + "/api/v1/clients", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0
