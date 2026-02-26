import allure
from scooter_api import ScooterApi
from data.order_data import TestData
from data.expected_data import ExpectedResponceCodes,ExpectedResponces

class TestAcceptOrder:

    @allure.title("Заказ можно принять")
    def test_accept_order(self, create_courier):
        order_response = ScooterApi.create_order(TestData.ORDER_PAYLOAD()) 
        track = order_response.json()["track"]
        order_data_response = ScooterApi.get_order_by_track(track)
        try:
            accept_response = ScooterApi.accept_order(order_data_response.json()["order"]["id"],create_courier["id"])
        finally:
            ScooterApi.cancel_order(track)
        assert accept_response.status_code == ExpectedResponceCodes.ACCEPT_ORDER_SUCCESS
        assert accept_response.json() == ExpectedResponces.ACCEPT_ORDER_SUCCESS
    
    @allure.title("Если не передать id курьера при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_without_courier_id(self):
        order_response = ScooterApi.create_order(TestData.ORDER_PAYLOAD())
        track = order_response.json()["track"]
        order_data_response = ScooterApi.get_order_by_track(track)
        try:
            accept_response = ScooterApi.accept_order(order_id=order_data_response.json()["order"]["id"])
        finally:
            ScooterApi.cancel_order(track)

        assert accept_response.status_code == ExpectedResponceCodes.ACCEPT_ORDER_WITHOUT_COURIER_ID
        assert accept_response.json()["message"] == ExpectedResponces.ACCEPT_ORDER_WITHOUT_COURIER_ID

    @allure.title("Если передать неверный id курьера при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_courier_id(self):
        order_response = ScooterApi.create_order(TestData.ORDER_PAYLOAD())
        track = order_response.json()["track"]
        order_data_response = ScooterApi.get_order_by_track(track)
        try:
            accept_response = ScooterApi.accept_order(order_data_response.json()["order"]["id"],TestData.NONEXISTENT_ID)
        finally:    
            ScooterApi.cancel_order(track)
        assert accept_response.status_code == ExpectedResponceCodes.ACCEPT_ORDER_WITH_NONEXISTENT_COURIER_ID
        assert accept_response.json()["message"] == ExpectedResponces.ACCEPT_ORDER_WITH_NONEXISTENT_COURIER_ID    


    @allure.title("Если не передать id заказа при принятии заказа, запрос вернёт ошибку")
    def test_accept_order_without_order_id(self, create_courier):
        accept_response = ScooterApi.accept_order(courier_id=create_courier["id"])

        assert accept_response.status_code == ExpectedResponceCodes.ACCEPT_ORDER_WITHOUT_ORDER_ID
        assert accept_response.json()["message"] == ExpectedResponces.ACCEPT_ORDER_WITHOUT_ORDER_ID


    @allure.title("Если передать неверный id заказа, запрос вернёт ошибку")
    def test_accept_order_with_nonexistent_order_id(self, create_courier):
        accept_response = ScooterApi.accept_order(TestData.NONEXISTENT_ID,create_courier["id"])
        
        assert accept_response.status_code ==ExpectedResponceCodes.ACCEPT_ORDER_WITH_NONEXISTENT_ORDER_ID
        assert accept_response.json()["message"] ==ExpectedResponces.ACCEPT_ORDER_WITH_NONEXISTENT_ORDER_ID