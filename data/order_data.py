from helpers.users import generate_random_string

class TestData:

    ORDER_COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]
    
    COURIER_DATA=[{"login": generate_random_string(10),"password": generate_random_string(10)},
                  {"login": generate_random_string(10),"firstName": generate_random_string(10)},
                  {"password": generate_random_string(10),"firstName": generate_random_string(10)}
                ]

    NONEXISTENT_ID=9999999

    @staticmethod
    def ORDER_PAYLOAD(color=["BLACK"]):
        return {"firstName": "Test",
                "lastName": "User",
                "address": "Test street",
                "metroStation": 4,
                "phone": "+79999999999",
                "rentTime": 5,
                "deliveryDate": "2025-02-20",
                "comment": "Test",
                "color": color
                }
    