import jsonschema
import inspect
import allure
from endpoints.endpoints_handler import Requests
from jsonschema.exceptions import ValidationError


def assert_check(act_result, exp_result, message):
    stack = inspect.stack()
    name_function = stack[1].function
    print(f'Start checking: {name_function}')
    print(f'Actual result= {act_result}\n')
    print(f'Expected result= {exp_result}\n')
    assert act_result == exp_result, f'\n{message}\n' \
                                     f'Actual_result = {act_result}\n'\
                                     f'Expected_result = {exp_result}\n'
    print(f'Done checking: {name_function}')


def body_in_response_loop(act_response, exp_response):
    print(f'Actual body= {act_response}\n')
    print(f'Expected body= {exp_response}\n')
    for key in exp_response.keys():
        actual_key = act_response.get(key)
        expected_key = exp_response[key]
        assert_check(actual_key, expected_key, '--Error check_body_in_response--')


class CheckResponse(Requests):
    @allure.step('Check response status is 201')
    def check_response_status_post_is_201(self):
        assert_check(self.status, 201, '--Error check_response_status_post_is_201--')


    @allure.step('Check response status is 200')
    def check_response_status_post_is_200(self):
        assert_check(self.status, 200, '--Error check_response_status_post_is_200--')

    @allure.step('Check body in response')
    def check_body_in_response(self, body_request=None):
        match body_request:
            case None:
                body_in_response_loop(self.body_response, self.body_request)
            case _:
                body_in_response_loop(self.body_response, body_request)


    @allure.step('Check json schema response')
    def check_jsonschema(self, json_schema):
        if self.body_user:
            print('Skip check jsonschema')
        else:
            try:
                jsonschema.validate(self.body_response, json_schema)
            except ValidationError as e:
                error_message = f"\n--Error in check_jsonschema--\n{e.message}"
                raise ValidationError(error_message) from None


    @allure.step('Check counts body in response')
    def check_cont_body_in_response(self):
        cont_body_response = len(self.body_response)
        exp_count = 100
        assert_check(cont_body_response, exp_count, '--Error check_body_in_response--')


    @allure.step('Check correct id number in response')
    def check_response_id_number(self, id_number):
        assert_check(self.id_number, id_number, '--Error check_id_response--')
