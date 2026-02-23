import pytest
import requests
import allure
from data.order_data import order_colors

class TestCreateOrder:

    @pytest.mark.parametrize("colors", order_colors)
    @allure.title("Создание заказа с разными цветами или без указания цвета")
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
        order_track=response.json()["track"]
        
        response_get_order = requests.get(f"{base_url}/orders/track?t="+ str(order_track))
        order_data=response_get_order.json()

        requests.put(f"{base_url}/orders/cancel?track="+str(order_track))

        assert response.status_code == 201
        assert "order" in order_data

