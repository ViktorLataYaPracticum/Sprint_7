import pytest
import allure
from scooter_api import ScooterApi
from data.order_data import TestData
from data.expected_data import ExpectedResponceCodes,ExpectedResponces


class TestCreateOrder:

    @pytest.mark.parametrize("colors", TestData.ORDER_COLORS)
    @allure.title("Создание заказа с разными цветами или без указания цвета")
    def test_create_order(self, colors):
        response = ScooterApi.create_order(TestData.ORDER_PAYLOAD(color=colors))
        order_track=response.json()["track"]

        response_get_order = ScooterApi.get_order_by_track(order_track)
        order_data=response_get_order.json()
        
        ScooterApi.cancel_order(order_track)

        assert response.status_code == ExpectedResponceCodes.CREATE_ORDER
        assert ExpectedResponces.CREATE_ORDER in order_data
        
        

