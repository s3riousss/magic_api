from exp_result.exp_json_schema import post_create
import allure


@allure.feature('Check request jsonplaceholder.typicode.com/posts')
@allure.story('Check post_create id')
def test_post(check_response, start_end_print):
    id_post = check_response.create_new_post()
    check_response.check_response_status_post_is_201()
    check_response.check_body_in_response()
    check_response.check_jsonschema(post_create)
    check_response.delete_request_id(id_post)
