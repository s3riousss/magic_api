import requests
import os
import dotenv
import json
import allure


class Requests:
    status = None
    body_response = None
    body_request = None
    body_user = False
    get_response = None
    id_number = None
    dotenv.load_dotenv()
    BASE_BODY = json.loads(str(os.getenv('BASE_BODY')))
    BASE_HEADERS = json.loads(str(os.getenv('BASE_HEADERS')))
    BASE_URL = os.getenv('BASE_URL')
    print(BASE_URL)


    @allure.step('Post request create for check')
    def create_new_post(self, body=BASE_BODY, url=BASE_URL, headers=BASE_HEADERS):
        if body != self.BASE_BODY:
            self.body_user = True
        response = requests.post(
            url=url,
            headers=headers,
            json=body
        )
        self.body_request = body
        self.status = response.status_code
        self.body_response = response.json()
        print(response.json())
        return response.json()['id']


    @allure.step('Get request for check')
    def get_request_id(self, id_post='', url=BASE_URL):
        if id_post == '':
            response = requests.get(
                url=url
            )
        else:
            response = requests.get(
                url=url + f'/{id_post}'
            )
        self.body_response = response.json()
        self.status = response.status_code
        return response.json()


    @allure.step('Put/patch request create for check')
    def put_or_patch_request_id(self, id_post, data, method, list_body='', url=BASE_URL):
        match method:
            case 'patch':
                response = requests.patch(
                    url=url + f'/{id_post}',
                    data=data
                )
                for elm in list_body:
                    if elm['id'] == id_post:
                        exp_data = elm
                exp_data.update(data)
                self.body_request = exp_data
            case 'put':
                response = requests.put(
                    url=url + f'/{id_post}',
                    data=data
                )
                self.body_request = data
        self.body_response = response.json()
        self.status = response.status_code
        self.id_number = response.json().get('id')


    @allure.step('Delete request for check')
    def delete_request_id(self, id_post, url=BASE_URL):
        response = requests.delete(
            url=url + f'/{id_post}'
        )
        self.body_response = response.json()
        self.status = response.status_code
