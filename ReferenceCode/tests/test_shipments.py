import requests
import pytest

BASE_URL = "http://localhost:3000"
API_KEY = "a1b2c3d4e5"

@pytest.mark.run(order=1)
def test_get_shipments():
    response = requests.get(BASE_URL + "/api/v1/shipments", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=2)
def test_create_shipment():
    body = {
        "id": 1,
        "order_id": 1,
        "source_id": 33,
        "order_date": "2000-03-09",
        "request_date": "2000-03-11",
        "shipment_date": "2000-03-13",
        "shipment_type": "I",
        "shipment_status": "Pending",
        "notes": "Zee vertrouwen klas rots heet lachen oneven begrijpen.",
        "carrier_code": "DPD",
        "carrier_description": "Dynamic Parcel Distribution",
        "service_code": "Fastest",
        "payment_type": "Manual",
        "transfer_mode": "Ground",
        "total_package_count": 31,
        "total_package_weight": 594.42,
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            },
            {
                "item_id": "P009557",
                "amount": 1
            }
        ]
    }
    response = requests.post(BASE_URL + "/api/v1/shipments", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 201

@pytest.mark.run(order=3)
def test_get_shipments():
    response = requests.get(BASE_URL + "/api/v1/shipments", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    shipments = response.json()
    assert len(shipments) == 1

@pytest.mark.run(order=4)
def test_get_shipment():
    response = requests.get(BASE_URL + "/api/v1/shipments/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    shipment = response.json()
    assert shipment["id"] == 1
    assert shipment["order_id"] == 1
    assert shipment["source_id"] == 33
    assert shipment["order_date"] == "2000-03-09"
    assert shipment["request_date"] == "2000-03-11"
    assert shipment["shipment_date"] == "2000-03-13"
    assert shipment["shipment_type"] == "I"
    assert shipment["shipment_status"] == "Pending"
    assert shipment["notes"] == "Zee vertrouwen klas rots heet lachen oneven begrijpen."
    assert shipment["carrier_code"] == "DPD"
    assert shipment["carrier_description"] == "Dynamic Parcel Distribution"
    assert shipment["service_code"] == "Fastest"
    assert shipment["payment_type"] == "Manual"
    assert shipment["transfer_mode"] == "Ground"
    assert shipment["total_package_count"] == 31
    assert shipment["total_package_weight"] == 594.42
    assert len(shipment["items"]) == 2
    assert shipment["items"][0]["item_id"] == "P007435"
    assert shipment["items"][0]["amount"] == 23
    assert shipment["items"][1]["item_id"] == "P009557"
    assert shipment["items"][1]["amount"] == 1

@pytest.mark.run(order=5)
def test_update_shipment():
    body = {
        "shipment_date": "2000-03-14",
        "shipment_status": "Shipped",
        "notes": "Updated notes.",
        "carrier_code": "UPS",
        "carrier_description": "United Parcel Service",
        "service_code": "Express",
        "payment_type": "Prepaid",
        "transfer_mode": "Air",
        "total_package_count": 32,
        "total_package_weight": 600.00,
        "items": [
            {
                "item_id": "P007435",
                "amount": 25
            },
            {
                "item_id": "P009557",
                "amount": 2
            }
        ]
    }
    response = requests.put(BASE_URL + "/api/v1/shipments/1", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 200

@pytest.mark.run(order=6)
def test_get_shipment():
    response = requests.get(BASE_URL + "/api/v1/shipments/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    shipment = response.json()
    assert shipment["id"] == 1
    assert shipment["shipment_date"] == "2000-03-14"
    assert shipment["shipment_status"] == "Shipped"
    assert shipment["notes"] == "Updated notes."
    assert shipment["carrier_code"] == "UPS"
    assert shipment["carrier_description"] == "United Parcel Service"
    assert shipment["service_code"] == "Express"
    assert shipment["payment_type"] == "Prepaid"
    assert shipment["transfer_mode"] == "Air"
    assert shipment["total_package_count"] == 32
    assert shipment["total_package_weight"] == 600.00
    assert len(shipment["items"]) == 2
    assert shipment["items"][0]["item_id"] == "P007435"
    assert shipment["items"][0]["amount"] == 25
    assert shipment["items"][1]["item_id"] == "P009557"
    assert shipment["items"][1]["amount"] == 2

@pytest.mark.run(order=7)
def test_get_shipment_orders():
    response = requests.get(BASE_URL + "/api/v1/shipments/1/orders", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=8)
def test_delete_shipment():
    response = requests.delete(BASE_URL + "/api/v1/shipments/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 204

@pytest.mark.run(order=9)
def test_get_shipments():
    response = requests.get(BASE_URL + "/api/v1/shipments", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0
