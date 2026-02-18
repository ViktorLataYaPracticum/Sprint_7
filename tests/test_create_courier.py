import requests
import allure

class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, base_url):
        payload = {
            "login": "unique_login_12345",
            "password": "1234",
            "firstName": "Test"
        }

        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, base_url):
        payload = {
            "login": "duplicate_login",
            "password": "1234",
            "firstName": "Test"
        }

        requests.post(f"{base_url}/courier", data=payload)
        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 409
        assert "message" in response.json()
