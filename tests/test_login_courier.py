import requests
import allure
from helpers.users import generate_random_string

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

    @allure.title("Авторизация без передачи логина")
    def test_login_without_login(self, base_url, create_courier):
        payload = {
            "password": create_courier["password"]
        }

        response = requests.post(f"{base_url}/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"]=="Недостаточно данных для входа"
    
    @allure.title("Авторизация с передачей неправильных логина или пароля")
    def test_login_wrong_autorization_data(self, base_url, create_courier):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = requests.post(f"{base_url}/courier/login", data=payload)

        assert response.status_code == 404
        assert response.json()["message"]=="Учетная запись не найдена"

    @allure.title("Авторизация без передачи пароля")
    def test_login_without_password(self, base_url, create_courier):
        payload = {
            "login": create_courier["login"]
        }

        response = requests.post(f"{base_url}/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"]=="Недостаточно данных для входа"

    @allure.title("Авторизация без передачи пары логин/пароль")
    def test_login_empty_data(self, base_url, create_courier):
        payload = {}

        response = requests.post(f"{base_url}/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"]=="Недостаточно данных для входа"



