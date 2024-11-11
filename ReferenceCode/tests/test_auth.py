import pytest
import requests
from urls import endpoints

def test_authorization():
    headers = {"API_KEY": "a1b2c3d4e5"}
    for endpoint in endpoints:
        url = f"http://localhost:3000{endpoint}".replace("{id}", "1")
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    headers = {"API_KEY": "invalid_key"}
    for endpoint in endpoints:
        url = f"http://localhost:3000{endpoint}".replace("{id}", "1")
        response = requests.get(url, headers=headers)
        assert response.status_code == 401