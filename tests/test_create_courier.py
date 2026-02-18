import requests
import allure
from helpers.users import generate_random_string

class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, base_url):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, base_url):
        dublicate_login=generate_random_string(10)
        payload = {
            "login": dublicate_login,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        requests.post(f"{base_url}/courier", data=payload)
        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 409
        assert "message" in response.json()

    @allure.title("Нельзя создать курьера без имени")
    def test_create_courier_without_first_name(self, base_url):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 400
        assert "message" in response.json()
        

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self, base_url):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 400
        assert "message" in response.json()
   
    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self, base_url):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(f"{base_url}/courier", data=payload)

        assert response.status_code == 400
        assert "message" in response.json()
