from exp_result.exp_json_schema import patch_change
import allure
from jsonschema import ValidationError


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check patch_request_id')
def test_put_request_id(check_response, start_end_print, random_string, random_id):
    list_body = check_response.get_request_id()
    data = {
        'title': random_string,
    }
    id_random = random_id
    check_response.put_or_patch_request_id(id_random, data, 'patch', list_body)
    try:
        check_response.check_response_status_post_is_200()
    except AssertionError as e:
        errors.append(str(e))
    try:
        check_response.check_body_in_response()
    except AssertionError as e:
        errors.append(str(e))
    try:
        check_response.check_jsonschema(patch_change)
    except ValidationError as e:
        errors.append(str(e))
    try:
        check_response.check_response_id_number(id_random)
    except ValidationError as e:
        errors.append(str(e))

    check_response.delete_request_id(id_random)

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
