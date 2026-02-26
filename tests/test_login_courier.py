import allure
from helpers.users import generate_random_string
from scooter_api import ScooterApi
from data.expected_data import ExpectedResponceCodes,ExpectedResponces

class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_success(self, create_courier):
        response = ScooterApi.login_courier({
                                            "login": create_courier["login"],
                                            "password": create_courier["password"]
                                            })
        assert response.status_code == ExpectedResponceCodes.LOGIN_SUCCESS
        assert ExpectedResponces.LOGIN_SUCCESS in response.json()

    @allure.title("Авторизация без передачи логина")
    def test_login_without_login(self, create_courier):
        response = ScooterApi.login_courier({"password": create_courier["password"]})
        assert response.status_code == ExpectedResponceCodes.LOGIN_WITHOUT_LOGIN
        assert response.json()["message"]==ExpectedResponces.LOGIN_WITHOUT_LOGIN
    
    @allure.title("Авторизация с передачей неправильных логина или пароля")
    def test_login_wrong_autorization_data(self):
        response = ScooterApi.login_courier({
                                             "login": generate_random_string(10),
                                             "password": generate_random_string(10)
                                             })
        assert response.status_code ==ExpectedResponceCodes.LOGIN_WRONG_AUTORIZATION_DATA
        assert response.json()["message"]==ExpectedResponces.LOGIN_WRONG_AUTORIZATION_DATA

    @allure.title("Авторизация без передачи пароля")
    def test_login_without_password(self, create_courier):
        response =ScooterApi.login_courier({"login": create_courier["login"]})
        assert response.status_code == ExpectedResponceCodes.LOGIN_WITHOUT_PASSWORD
        assert response.json()["message"]==ExpectedResponces.LOGIN_WITHOUT_PASSWORD

    @allure.title("Авторизация без передачи пары логин/пароль")
    def test_login_empty_data(self, create_courier):
        response = ScooterApi.login_courier({})
        assert response.status_code == ExpectedResponceCodes.LOGIN_EMPTY_DATA
        assert response.json()["message"]==ExpectedResponces.LOGIN_EMPTY_DATA



