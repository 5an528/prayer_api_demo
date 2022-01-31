import allure
from test_data.users_api.prayers_api_data import *


@allure.step('get prayer month times')
def test_07_month_prayer_times():
    response_body, status_code = response_get_times_month()
    print(response_body)
    assert status_code == 200
