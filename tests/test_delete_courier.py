import allure
from scooter_api import ScooterApi
from data.order_data import TestData
from data.expected_data import ExpectedResponceCodes,ExpectedResponces

class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, create_courier):
        response = ScooterApi.delete_courier(create_courier['id'])
        assert response.status_code == ExpectedResponceCodes.DELETE_COURIER_SUCCESS
        assert response.json() == ExpectedResponces.DELETE_COURIER_SUCCESS

    @allure.title("Запрос удаления курьера без передачи id возвращает ошибку")
    def test_delete_courier_without_id(self):
        response = ScooterApi.delete_courier()
        assert response.status_code == ExpectedResponceCodes.DELETE_COURIER_WITHOUT_ID
        assert response.json()["message"] == ExpectedResponces.DELETE_COURIER_WITHOUT_ID

    @allure.title("Запрос удаления курьера с передачей несуществующего id возвращает ошибку")
    def test_delete_courier_with_nonexistent_id(self):
        response = ScooterApi.delete_courier(TestData.NONEXISTENT_ID)
        assert response.status_code == ExpectedResponceCodes.DELETE_COURIER_WITH_NONEXISTENT_ID
        assert response.json()["message"] == ExpectedResponces.DELETE_COURIER_WITH_NONEXISTENT_ID
