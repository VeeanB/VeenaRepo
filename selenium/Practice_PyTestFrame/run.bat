@REM pytest -v -s -m "regression" --browser chrome TestCases
@REM pytest -v -s -m "regression" --browser firefox TestCases
@REM pytest -v -s -m "regression" --browser edge TestCases
pytest -v -s TestCases/Test_Login.py


@rem start pytest -v -s --html=reports\report_chrome.html testCases\Test_Login.py --browser chrome
@REM start pytest -v -s --html=reports\report_edge.html testCases\Test_Login.py --browser edge
@REM start pytest -v -s --html=reports\report_firfox.html testCases\Test_Login.py --browser firefox
