import allure
import requests
from urls import Urls

class ScooterApi:

    @staticmethod
    @allure.step("Создать заказ")
    def create_order(order_payload):
       return requests.post(f"{Urls.BASE_URL}/orders", json=order_payload)
    
    @staticmethod
    @allure.step("Получить заказ по номеру отслеживания")
    def get_order_by_track(track=None):
        if (track):
            return requests.get(f"{Urls.BASE_URL}/orders/track?t={track}")
        else:
            return requests.get(f"{Urls.BASE_URL}/orders/track")
    
    @staticmethod
    @allure.step("Принять заказ")
    def accept_order(order_id=None,courier_id=None):
        if (not order_id):
            return requests.put(f"{Urls.BASE_URL}/orders/accept/?courierId={courier_id}" )
        elif (not courier_id):
            return requests.put(f"{Urls.BASE_URL}/orders/accept/{order_id}" )
        else:
            return requests.put(f"{Urls.BASE_URL}/orders/accept/{order_id}/?courierId={courier_id}" )
    
    @staticmethod
    @allure.step("Отменить заказ")
    def cancel_order(track=None):
        if (track):
            return requests.put(f"{Urls.BASE_URL}/orders/cancel?track={track}")
        else:    
            return requests.put(f"{Urls.BASE_URL}/orders/cancel")

    @staticmethod
    @allure.step("Получить список заказов")
    def get_orders_list():
        return requests.get(f"{Urls.BASE_URL}/orders")
    
    @staticmethod
    @allure.step("Удалить курьера")
    def delete_courier(courier_id=None):
        if (courier_id):
            return requests.delete(f"{Urls.BASE_URL}/courier/{courier_id}")
        else:
            return requests.delete(f"{Urls.BASE_URL}/courier/")
        
    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(payload):
        return requests.post(f"{Urls.BASE_URL}/courier/login", data=payload)
    
    @staticmethod
    @allure.step("Создать курьера")
    def create_courier(payload):
        return requests.post(f"{Urls.BASE_URL}/courier", data=payload)