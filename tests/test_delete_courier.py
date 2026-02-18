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
