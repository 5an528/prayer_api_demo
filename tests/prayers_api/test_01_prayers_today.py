import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get today prayer times')
def test_01_today_prayer_times():
    response_body, status_code = response_get_times_today()
    print(response_body)
    assert status_code == 200

