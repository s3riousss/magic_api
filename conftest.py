import pytest
import random
import string
from endpoints.create_body_endpoint import CreateIdEndpoint
from endpoints.get_requests import GetIdEndpoint
from endpoints.check_response import CheckResponse


@pytest.fixture()
def creator_body_endp():
    return CreateIdEndpoint()


@pytest.fixture()
def get_requests():
    return GetIdEndpoint()


@pytest.fixture()
def check_response():
    return CheckResponse()


@pytest.fixture(scope='session')
def start_end_print():
    yield print('\n--Start check--\n')
    print('\n--End check--\n')


@pytest.fixture()
def random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 12)))


@pytest.fixture()
def random_id():
    return random.randint(1, 100)
