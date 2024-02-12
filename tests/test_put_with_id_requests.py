from exp_result.exp_json_schema import put_response
import allure
from jsonschema import ValidationError


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check put_request_id')
def test_put_request_id(check_response, creator_body_endp, start_end_print, random_string, random_id):
    #  The service does not create a new id and you cannot change it, so this line is commented out
    # with allure.step('Post request create for put'):
    #     id_request = creator_body_endp.create_new_post()
    with allure.step('PUT request'):
        data = {
            'test0': random_string,
        }
        id_random = random_id
        check_response.put_or_patch_request_id(id_random, data, 'put')
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
            check_response.check_jsonschema(put_response)
    except ValidationError as e:
        errors.append(str(e))

    try:
        with allure.step('Check correct id number in response'):
            check_response.check_response_id_number(id_random)
    except ValidationError as e:
        errors.append(str(e))

    with allure.step('Delete request'):
        check_response.delete_request_id(id_random)

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
