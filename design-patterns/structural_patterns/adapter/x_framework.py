from src import some_route


def post_http():
    http_message = {
        "method": "POST",
        "header": {
            "token": "Bearer jioiaefi48904729kldan324",
            "origin": "http://something.other.org"
        },
        "body": {
            "name": "Lhama",
            "message": "Hello Word"
        }
    }

    some_route(http_message)
