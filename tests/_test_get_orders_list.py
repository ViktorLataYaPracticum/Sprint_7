import requests
import allure

class TestGetOrdersList:

    @allure.title("Возвращается список заказов")
    def test_get_orders_list(self, base_url):
        response = requests.get(f"{base_url}/orders")

        assert response.status_code == 200
        assert "orders" in response.json()
