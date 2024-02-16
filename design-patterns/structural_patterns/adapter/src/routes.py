from .controller import write_in_database
from .helper import Adapter


def some_route(message):
    process = Adapter(HttpRequest())
    process.handle(message)


class HttpRequest:
    def handle(self, message):
        token = message['header']['token']

        if token:
            print('Authenticating token')
            write_in_database(
                message['body']['name'],
                message['body']['message']
            )
