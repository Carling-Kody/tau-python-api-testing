import requests

from config import BASE_URL
from utils.print_helpers import pretty_print
from uuid import uuid4
from json import dumps
from assertpy.assertpy import assert_that


def test_read_all_has_kent():
    response = requests.get(BASE_URL)
    response_text = response.json()
    pretty_print(response_text)

    assert_that(response.status_code).is_equal_to(200)
    first_names = [people['fname'] for people in response_text]
    assert_that(first_names).contains('Kent')
