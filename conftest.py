import pytest
import requests
from helpers.users import register_new_courier_and_return_login_password
from urls import Urls


@pytest.fixture
def create_courier():
    courier_data = register_new_courier_and_return_login_password()

    assert courier_data, "Курьер не был создан через helper"

    login, password, _ = courier_data

    login_payload = {
        "login": login,
        "password": password
    }

    response = requests.post(f"{Urls.BASE_URL}/courier/login", data=login_payload)
    courier_id = response.json()["id"]

    yield {
        "login": login,
        "password": password,
        "id": courier_id
    }

    requests.delete(f"{Urls.BASE_URL}/courier/{courier_id}")
