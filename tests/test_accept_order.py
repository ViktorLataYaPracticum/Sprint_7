import requests
import allure
import logging

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
        order_data_response = requests.get(f"{base_url}/orders/track?t={track}")
        order_id=order_data_response.json()["order"]["id"]

        accept_response = requests.put(f"{base_url}/orders/accept/{order_id}/?courierId={create_courier["id"]}" )
        requests.put(f"{base_url}/orders/cancel?track={track}")
        
        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}

    @allure.title("Если не передать id курьера при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_without_courier_id(self, base_url):
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
        order_data_response = requests.get(f"{base_url}/orders/track?t={track}")
        order_id=order_data_response.json()["order"]["id"]

        accept_response = requests.put(f"{base_url}/orders/accept/{order_id}")
        requests.put(f"{base_url}/orders/cancel?track={track}")

        assert accept_response.status_code == 400
        assert accept_response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Если передать неверный id курьера при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_courier_id(self, base_url):
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
        order_data_response = requests.get(f"{base_url}/orders/track?t={track}")
        order_id=order_data_response.json()["order"]["id"]

        accept_response = requests.put(f"{base_url}/orders/accept/{order_id}/?courierId=9999999")
        requests.put(f"{base_url}/orders/cancel?track={track}")

        assert accept_response.status_code == 404
        assert accept_response.json()["message"] == "Курьера с таким id не существует"    

    @allure.title("Если не передать id заказа при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_without_order_id(self, base_url, create_courier):
        accept_response = requests.put(f"{base_url}/orders/accept/?courierId={create_courier["id"]}" )
        
        assert accept_response.status_code == 400
        assert accept_response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Если передать неверный id заказа, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_order_id(self, base_url, create_courier):
        accept_response = requests.put(f"{base_url}/orders/accept/9999999/?courierId={create_courier["id"]}" )
        
        assert accept_response.status_code == 404
        assert accept_response.json()["message"] == "Заказа с таким id не существует"