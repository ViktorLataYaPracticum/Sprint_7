import requests
import allure

class TestGetOrderByTrack:

    @allure.title("Можно получить заказ по номеру")
    def test_get_order_by_track(self, base_url):
        order_payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test street",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-02-20",
            "comment": "Test",
            "color": ["GREY"]
        }

        create_response = requests.post(f"{base_url}/orders", json=order_payload)
        track = create_response.json()["track"]

        response = requests.get(
            f"{base_url}/orders/track",
            params={"t": track}
        )

        assert response.status_code == 200
        assert "order" in response.json()
