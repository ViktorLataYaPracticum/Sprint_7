class ExpectedResponceCodes:
    #Принять заказ
    ACCEPT_ORDER_SUCCESS=200
    ACCEPT_ORDER_WITHOUT_COURIER_ID=400
    ACCEPT_ORDER_WITH_NONEXISTENT_COURIER_ID=404
    ACCEPT_ORDER_WITHOUT_ORDER_ID=400
    ACCEPT_ORDER_WITH_NONEXISTENT_ORDER_ID=404
     
    #Получить список заказов
    GET_ORDERS_LIST=200
    
    #Удаление курьера
    DELETE_COURIER_SUCCESS=200
    DELETE_COURIER_WITHOUT_ID=400
    DELETE_COURIER_WITH_NONEXISTENT_ID=404

    #Создание заказа
    CREATE_ORDER=201
    
    #Получить заказ по номеру трека
    GET_ORDER_BY_TRACK=200
    GET_ORDER_WITHOUT_TRACK=400
    GET_ORDER_WITH_NONEXISTENT_TRACK=404

    #Авторизация курьера
    LOGIN_SUCCESS=200
    LOGIN_WITHOUT_LOGIN=400
    LOGIN_WRONG_AUTORIZATION_DATA=404
    LOGIN_WITHOUT_PASSWORD=400
    LOGIN_EMPTY_DATA=400

    #Создание нового курьера
    CREATE_COURIER_SUCCESS=201
    CREATE_DUPLICATE_COURIER=409
    CREATE_COURIER_WITHOUT_ANY_PARAM=400

class ExpectedResponces:
    #Принять заказ
    ACCEPT_ORDER_SUCCESS={"ok": True}
    ACCEPT_ORDER_WITHOUT_COURIER_ID="Недостаточно данных для поиска"
    ACCEPT_ORDER_WITH_NONEXISTENT_COURIER_ID="Курьера с таким id не существует"
    ACCEPT_ORDER_WITHOUT_ORDER_ID="Недостаточно данных для поиска"
    ACCEPT_ORDER_WITH_NONEXISTENT_ORDER_ID="Заказа с таким id не существует"

    #Получить список заказов
    GET_ORDERS_LIST="orders"

    #Удаление курьера
    DELETE_COURIER_SUCCESS={"ok": True}
    DELETE_COURIER_WITHOUT_ID="Недостаточно данных для удаления курьера"
    DELETE_COURIER_WITH_NONEXISTENT_ID="Курьера с таким id нет"

    #Создание заказа
    CREATE_ORDER="order"

    #Получить заказ по номеру трека
    GET_ORDER_BY_TRACK="order"
    GET_ORDER_WITHOUT_TRACK="Недостаточно данных для поиска"
    GET_ORDER_WITH_NONEXISTENT_TRACK="Заказ не найден"

    #Авторизация курьера
    LOGIN_SUCCESS="id"
    LOGIN_WITHOUT_LOGIN="Недостаточно данных для входа"
    LOGIN_WRONG_AUTORIZATION_DATA="Учетная запись не найдена"
    LOGIN_WITHOUT_PASSWORD="Недостаточно данных для входа"
    LOGIN_EMPTY_DATA="Недостаточно данных для входа"

    #Создание нового курьера
    CREATE_COURIER_SUCCESS={"ok": True}
    CREATE_DUPLICATE_COURIER="Этот логин уже используется"
    CREATE_COURIER_WITHOUT_ANY_PARAM="Недостаточно данных для создания учетной записи"

