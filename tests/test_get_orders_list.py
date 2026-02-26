import allure
from scooter_api import ScooterApi
from data.expected_data import ExpectedResponceCodes,ExpectedResponces


class TestGetOrdersList:

    @allure.title("Возвращается список заказов")
    def test_get_orders_list(self):
        response = ScooterApi.get_orders_list()
        assert response.status_code == ExpectedResponceCodes.GET_ORDERS_LIST
        assert ExpectedResponces.GET_ORDERS_LIST in response.json()
