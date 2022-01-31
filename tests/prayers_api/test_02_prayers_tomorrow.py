import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get tomorrow prayer times')
def test_02_tomorrow_prayer_times():
    response_body, status_code = response_get_times_tomorrow()
    print(response_body)
    assert status_code == 200
