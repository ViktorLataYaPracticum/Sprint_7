import requests
import allure

class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, base_url, create_courier):
        payload = {
            "login": create_courier["login"],
            "password": create_courier["password"]
        }

        response = requests.post(f"{base_url}/courier/login", data=payload)

        assert response.status_code == 200
        assert "id" in response.json()
