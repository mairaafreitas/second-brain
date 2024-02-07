from src import some_route

def post_http():
    http_message = {
        "HTTP_method": "POST",
        "HTTP_header": [
            ("token", "Bearer jioiaefi48904729kldan324"),
            ("origin", "http://something.other.org")
        ],
        "HTTP_body": [
            ("name", "Lhama"),
            ("message", "Hello Word")
        ]
    }

    some_route(http_message)