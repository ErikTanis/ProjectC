import requests
import pytest

BASE_URL = "http://localhost:3000"
API_KEY = "a1b2c3d4e5"

@pytest.mark.run(order=1)
def test_get_suppliers():
    response = requests.get(BASE_URL + "/api/v1/suppliers", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=2)
def test_create_supplier():
    body = {
        "id": 1,
        "code": "SUP0001",
        "name": "Lee, Parks and Johnson",
        "address": "5989 Sullivan Drives",
        "address_extra": "Apt. 996",
        "city": "Port Anitaburgh",
        "zip_code": "91688",
        "province": "Illinois",
        "country": "Czech Republic",
        "contact_name": "Toni Barnett",
        "phonenumber": "363.541.7282x36825",
        "reference": "LPaJ-SUP0001",
        "created_at": "1971-10-20 18:06:17",
        "updated_at": "1985-06-08 00:13:46"
    }
    response = requests.post(BASE_URL + "/api/v1/suppliers", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 201

@pytest.mark.run(order=3)
def test_get_suppliers():
    response = requests.get(BASE_URL + "/api/v1/suppliers", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    suppliers = response.json()
    assert len(suppliers) == 1

@pytest.mark.run(order=4)
def test_get_supplier():
    response = requests.get(BASE_URL + "/api/v1/suppliers/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    supplier = response.json()
    assert supplier["id"] == 1
    assert supplier["code"] == "SUP0001"
    assert supplier["name"] == "Lee, Parks and Johnson"
    assert supplier["address"] == "5989 Sullivan Drives"
    assert supplier["address_extra"] == "Apt. 996"
    assert supplier["city"] == "Port Anitaburgh"
    assert supplier["zip_code"] == "91688"
    assert supplier["province"] == "Illinois"
    assert supplier["country"] == "Czech Republic"
    assert supplier["contact_name"] == "Toni Barnett"
    assert supplier["phonenumber"] == "363.541.7282x36825"
    assert supplier["reference"] == "LPaJ-SUP0001"
    assert supplier["created_at"] == "1971-10-20 18:06:17"
    assert supplier["updated_at"] == "1985-06-08 00:13:46"

@pytest.mark.run(order=5)
def test_update_supplier():
    body = {
        "address": "1234 New Address",
        "address_extra": "Suite 100",
        "city": "New City",
        "zip_code": "12345",
        "province": "New Province",
        "country": "New Country",
        "contact_name": "New Contact",
        "phonenumber": "123-456-7890",
        "reference": "New-Reference",
        "updated_at": "2023-01-01 00:00:00"
    }
    response = requests.put(BASE_URL + "/api/v1/suppliers/1", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 200

@pytest.mark.run(order=6)
def test_get_supplier():
    response = requests.get(BASE_URL + "/api/v1/suppliers/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    supplier = response.json()
    assert supplier["address"] == "1234 New Address"
    assert supplier["address_extra"] == "Suite 100"
    assert supplier["city"] == "New City"
    assert supplier["zip_code"] == "12345"
    assert supplier["province"] == "New Province"
    assert supplier["country"] == "New Country"
    assert supplier["contact_name"] == "New Contact"
    assert supplier["phonenumber"] == "123-456-7890"
    assert supplier["reference"] == "New-Reference"
    assert supplier["updated_at"] == "2023-01-01 00:00:00"

@pytest.mark.run(order=7)
def test_delete_supplier():
    response = requests.delete(BASE_URL + "/api/v1/suppliers/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 204

@pytest.mark.run(order=8)
def test_get_suppliers():
    response = requests.get(BASE_URL + "/api/v1/suppliers", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0
