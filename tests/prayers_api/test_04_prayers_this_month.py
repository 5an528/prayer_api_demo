import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get this month prayer times')
def test_04_this_month_prayer_times():
    response_body, status_code = response_get_times_this_month()
    print(response_body)
    assert status_code == 200
