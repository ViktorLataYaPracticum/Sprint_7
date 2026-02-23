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

        response = requests.get(f"{base_url}/orders/track?t={track}")

        assert response.status_code == 200
        assert "order" in response.json()

    @allure.title("Запрос заказа без номера возвращает ошибку")
    def test_get_order_without_track(self, base_url):

        response = requests.get(f"{base_url}/orders/track?t=")

        assert response.status_code == 400
        assert response.json()["message"]=="Недостаточно данных для поиска"
    
    @allure.title("Запрос заказа с несуществующим номером заказа возвращает ошибку")
    def test_get_order_with_nonexistent_track(self, base_url):

        response = requests.get(f"{base_url}/orders/track?t=999999999")

        assert response.status_code == 404
        assert response.json()["message"]=="Заказ не найден"        
