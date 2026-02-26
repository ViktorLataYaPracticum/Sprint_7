import allure
from scooter_api import ScooterApi
from data.expected_data import ExpectedResponceCodes,ExpectedResponces
from data.order_data import TestData

class TestGetOrderByTrack:

    @allure.title("Можно получить заказ по номеру")
    def test_get_order_by_track(self):
        create_response =ScooterApi.create_order(TestData.ORDER_PAYLOAD(["GREY"]))
        response = ScooterApi.get_order_by_track(create_response.json()["track"])
        assert response.status_code == ExpectedResponceCodes.GET_ORDER_BY_TRACK
        assert ExpectedResponces.GET_ORDER_BY_TRACK in response.json()

    @allure.title("Запрос заказа без номера возвращает ошибку")
    def test_get_order_without_track(self):
        response = ScooterApi.get_order_by_track()
        assert response.status_code == ExpectedResponceCodes.GET_ORDER_WITHOUT_TRACK
        assert response.json()["message"]==ExpectedResponces.GET_ORDER_WITHOUT_TRACK
    
    @allure.title("Запрос заказа с несуществующим номером заказа возвращает ошибку")
    def test_get_order_with_nonexistent_track(self):
        response = ScooterApi.get_order_by_track(TestData.NONEXISTENT_ID)
        assert response.status_code == ExpectedResponceCodes.GET_ORDER_WITH_NONEXISTENT_TRACK
        assert response.json()["message"]== ExpectedResponces.GET_ORDER_WITH_NONEXISTENT_TRACK
