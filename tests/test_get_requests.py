import allure


errors = []


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check get_request')
def test_get_request(check_response, start_end_print):
    with allure.step('Get request for get'):
        check_response.get_request_id()
    try:
        with allure.step('Check response status is 200'):
            check_response.check_response_status_post_is_200()
    except AssertionError as e:
        errors.append(str(e))
    try:
        with allure.step('Check counts body in response'):
            check_response.check_cont_body_in_response()
    except AssertionError as e:
        errors.append(str(e))

    if errors:
        error_message = "Errors in tests:\n" + "\n".join(errors)
        raise AssertionError(error_message)
