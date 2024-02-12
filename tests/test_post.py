from exp_result.exp_json_schema import post_create
import allure


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check post_create id')
def test_post(check_response, start_end_print):
    with allure.step('Post request for create'):
        id_post = check_response.create_new_post()
    with allure.step('Check response status is 201'):
        check_response.check_response_status_post_is_201()
    with allure.step('Check body in response'):
        check_response.check_body_in_response()
    with allure.step('Check json schema response'):
        check_response.check_jsonschema(post_create)
    with allure.step('Delete request'):
        check_response.delete_request_id(id_post)
