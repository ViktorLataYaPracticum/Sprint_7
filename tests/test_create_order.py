import pytest
import requests
import allure
from data.order_data import order_colors

class TestCreateOrder:

    @pytest.mark.parametrize("colors", order_colors)
    @allure.title("Создание заказа с разными цветами")
    def test_create_order(self, base_url, colors):
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test street",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-02-20",
            "comment": "Test order",
            "color": colors
        }

        response = requests.post(f"{base_url}/orders", json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
