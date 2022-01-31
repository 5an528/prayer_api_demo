import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get this week prayer times')
def test_03_this_week_prayer_times():
    response_body, status_code = response_get_times_this_week()
    print(response_body)
    assert status_code == 200
