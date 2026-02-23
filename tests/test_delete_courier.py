import requests
import allure

class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, base_url, create_courier):
        response = requests.delete(
            f"{base_url}/courier/{create_courier['id']}"
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Запрос удаления курьера без передачи id возвращает ошибку")
    def test_delete_courier_without_id(self, base_url):
        response = requests.delete(
            f"{base_url}/courier/"
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для удаления курьера"

    @allure.title("Запрос удаления курьера с передачей несуществующего id возвращает ошибку")
    def test_delete_courier_with_nonexistent_id(self, base_url):
        response = requests.delete(
            f"{base_url}/courier/99999999"
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id нет"
