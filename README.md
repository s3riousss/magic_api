# magic_api
Steps to run the tests:
1) Clone project with SSH or HTTPS url
2) Install all module: 
**pip install -r requirements.txt**
3) For run test use:
**pytest tests --alluredir=allure_results**
4) For look results use:
**allure serve allure_results --host localhost --port 9999**
