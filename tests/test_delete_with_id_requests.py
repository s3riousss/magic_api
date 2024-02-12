from exp_result.exp_json_schema import delete_response
import allure
from jsonschema import ValidationError


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check delete_request_id')
def test_put_request_id(check_response, creator_body_endp, start_end_print, random_string):
    with allure.step('Post request create for delete'):
        id_request = creator_body_endp.create_new_post()
    with allure.step('Delete request'):
        check_response.delete_request_id(id_request)
    try:
        with allure.step('Check response status is 200'):
            check_response.check_response_status_post_is_200()
    except AssertionError as e:
        errors.append(str(e))
    try:
        with allure.step('Check body in response'):
            check_response.check_body_in_response(body_request={})
    except AssertionError as e:
        errors.append(str(e))
    try:
        with allure.step('Check json schema response'):
            check_response.check_jsonschema(delete_response)
    except ValidationError as e:
        errors.append(str(e))

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
