from endpoints.endpoints_handler import Requests
import requests


class CreateIdEndpoint(Requests):

    def create_new_post(
            self, body=None, url=None, headers=None
    ):
        if body is None:
            body = self.BASE_BODY
        if url is None:
            url = self.BASE_URL
        if headers is None:
            headers = self.BASE_HEADERS
        response = requests.post(
            url=url,
            headers=headers,
            json=body
        )
        return response.json()['id']
