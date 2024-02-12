from exp_result.exp_json_schema import post_create
import allure
from jsonschema import ValidationError


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check get_request_id')
def test_get_request_id(check_response, start_end_print):
    with allure.step('Post request for check id'):
        id_request = check_response.create_new_post()
    with allure.step('Get request for get id'):
        check_response.get_request_id(id_request)
    try:
        with allure.step('Check response status is 200'):
            check_response.check_response_status_post_is_200()
    except AssertionError as e:
        errors.append(str(e))
    try:
        with allure.step('Check body in response'):
            check_response.check_body_in_response()
    except AssertionError as e:
        errors.append(str(e))
    try:
        with allure.step('Check json schema response'):
            check_response.check_jsonschema(post_create)
    except ValidationError as e:
        errors.append(str(e))

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
