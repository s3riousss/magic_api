import allure


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check get_request')
def test_get_request(check_response, start_end_print):
    check_response.get_request_id()
    try:
        check_response.check_response_status_post_is_200()
    except AssertionError as e:
        errors.append(str(e))
    try:
        check_response.check_cont_body_in_response()
    except AssertionError as e:
        errors.append(str(e))

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
