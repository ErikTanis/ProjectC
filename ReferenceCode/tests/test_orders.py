import requests
import pytest

BASE_URL = "http://localhost:3000"
API_KEY = "a1b2c3d4e5"

@pytest.mark.run(order=1)
def test_get_orders():
    response = requests.get(BASE_URL + "/api/v1/orders", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.run(order=2)
def test_create_order():
    body = {
        "id": 1,
        "source_id": 33,
        "order_date": "2019-04-03T11:33:15Z",
        "request_date": "2019-04-07T11:33:15Z",
        "reference": "ORD00001",
        "reference_extra": "Bedreven arm straffen bureau.",
        "order_status": "Delivered",
        "notes": "Voedsel vijf vork heel.",
        "shipping_notes": "Buurman betalen plaats bewolkt.",
        "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
        "warehouse_id": 18,
        "ship_to": 1481,
        "bill_to": 7048,
        "shipment_id": 1,
        "total_amount": 9905.13,
        "total_discount": 150.77,
        "total_tax": 372.72,
        "total_surcharge": 77.6,
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
    response = requests.post(BASE_URL + "/api/v1/orders", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 201

@pytest.mark.run(order=3)
def test_get_orders():
    response = requests.get(BASE_URL + "/api/v1/orders", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    orders = response.json()
    assert len(orders) == 1

@pytest.mark.run(order=4)
def test_get_order():
    response = requests.get(BASE_URL + "/api/v1/orders/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    order = response.json()
    assert order["id"] == 1
    assert order["source_id"] == 33
    assert order["order_date"] == "2019-04-03T11:33:15Z"
    assert order["request_date"] == "2019-04-07T11:33:15Z"
    assert order["reference"] == "ORD00001"
    assert order["reference_extra"] == "Bedreven arm straffen bureau."
    assert order["order_status"] == "Delivered"
    assert order["notes"] == "Voedsel vijf vork heel."
    assert order["shipping_notes"] == "Buurman betalen plaats bewolkt."
    assert order["picking_notes"] == "Ademen fijn volgorde scherp aardappel op leren."
    assert order["warehouse_id"] == 18
    assert order["ship_to"] == 1481
    assert order["bill_to"] == 7048
    assert order["shipment_id"] == 1
    assert order["total_amount"] == 9905.13
    assert order["total_discount"] == 150.77
    assert order["total_tax"] == 372.72
    assert order["total_surcharge"] == 77.6
    assert len(order["items"]) == 2
    assert order["items"][0]["item_id"] == "P007435"
    assert order["items"][0]["amount"] == 23
    assert order["items"][1]["item_id"] == "P009557"
    assert order["items"][1]["amount"] == 1

@pytest.mark.run(order=5)
def test_update_order():
    body = {
        "order_status": "Shipped",
        "notes": "Updated notes.",
        "shipping_notes": "Updated shipping notes.",
        "picking_notes": "Updated picking notes.",
        "total_amount": 10000.00,
        "total_discount": 200.00,
        "total_tax": 400.00,
        "total_surcharge": 100.00,
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
    response = requests.put(BASE_URL + "/api/v1/orders/1", headers={"API_KEY": API_KEY}, json=body)
    assert response.status_code == 200

@pytest.mark.run(order=6)
def test_get_order():
    response = requests.get(BASE_URL + "/api/v1/orders/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    order = response.json()
    assert order["id"] == 1
    assert order["order_status"] == "Shipped"
    assert order["notes"] == "Updated notes."
    assert order["shipping_notes"] == "Updated shipping notes."
    assert order["picking_notes"] == "Updated picking notes."
    assert order["total_amount"] == 10000.00
    assert order["total_discount"] == 200.00
    assert order["total_tax"] == 400.00
    assert order["total_surcharge"] == 100.00
    assert len(order["items"]) == 2
    assert order["items"][0]["item_id"] == "P007435"
    assert order["items"][0]["amount"] == 25
    assert order["items"][1]["item_id"] == "P009557"
    assert order["items"][1]["amount"] == 2

@pytest.mark.run(order=7)
def test_get_order_items():
    response = requests.get(BASE_URL + "/api/v1/orders/1/items", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2

@pytest.mark.run(order=8)
def test_delete_order():
    response = requests.delete(BASE_URL + "/api/v1/orders/1", headers={"API_KEY": API_KEY})
    assert response.status_code == 204

@pytest.mark.run(order=9)
def test_get_orders():
    response = requests.get(BASE_URL + "/api/v1/orders", headers={"API_KEY": API_KEY})
    assert response.status_code == 200
    assert len(response.json()) == 0
