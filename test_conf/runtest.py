import os
from uitls_function import read_date, read_and_update_counter, keep_reports

report_folder_name = f"{read_date()}_{read_and_update_counter()}"

# For running testCases
command = f"pytest -s --alluredir=report_allure/{report_folder_name} --html=report_html/report_{report_folder_name}" \
          f".html --self-contained-html tests "
os.system(command)

# Number of allure & html reports to keep
number = 2
keep_reports(number, "report_allure", "report_html")

# For generating report
command = f"allure serve report_allure/{report_folder_name}"
os.system(command)
