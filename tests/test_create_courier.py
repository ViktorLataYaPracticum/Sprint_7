import allure
import pytest
from helpers.users import generate_random_string
from scooter_api import ScooterApi
from data.expected_data import ExpectedResponceCodes,ExpectedResponces
from data.order_data import TestData

class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = ScooterApi.create_courier(payload)
        assert response.status_code == ExpectedResponceCodes.CREATE_COURIER_SUCCESS
        assert response.json() == ExpectedResponces.CREATE_COURIER_SUCCESS

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        dublicate_login=generate_random_string(10)
        payload = {
            "login": dublicate_login,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        ScooterApi.create_courier(payload)
        response = ScooterApi.create_courier(payload) 
        assert response.status_code == ExpectedResponceCodes.CREATE_DUPLICATE_COURIER
        assert response.json()["message"]==ExpectedResponces.CREATE_DUPLICATE_COURIER

    @pytest.mark.parametrize("payload", TestData.COURIER_DATA)
    @allure.title("Нельзя создать курьера без любого из параметров")
    def test_create_courier_without_any_param(self,payload):
        response = ScooterApi.create_courier(payload)
        assert response.status_code == ExpectedResponceCodes.CREATE_COURIER_WITHOUT_ANY_PARAM
        assert response.json()["message"]==ExpectedResponces.CREATE_COURIER_WITHOUT_ANY_PARAM