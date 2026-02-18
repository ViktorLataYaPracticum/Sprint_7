import requests
import allure

class TestAcceptOrder:

    @allure.title("Заказ можно принять")
    def test_accept_order(self, base_url, create_courier):
        order_payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test street",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-02-20",
            "comment": "Test",
            "color": ["BLACK"]
        }

        order_response = requests.post(f"{base_url}/orders", json=order_payload)
        track = order_response.json()["track"]

        accept_response = requests.put(
            f"{base_url}/orders/accept",
            params={
                "id": track,
                "courierId": create_courier["id"]
            }
        )

        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}
