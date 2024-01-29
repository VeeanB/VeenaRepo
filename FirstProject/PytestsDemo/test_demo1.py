#Any pytest file should start with test_
#Any Pytest method should start with test_
#Any code should be wraped in method only
#Method name has sense
# -k stands for methods names execution, -s logs in out put -v stands for more info metadata
#you can run specific file with py.test<filename>
#you can mark (tag) tests @pytests.mark.smoke and then run with -m(grouping)
#you can skip step with skip
#you can skip step in the report after eecuting step @pytest.mark.xfail
#fixture is used to broswer setup like prerequiestion
#fixtures are used as setup and tear down methods for test cases - conftest file to generalize
#fixture and make it avaible to all test cases
#datadrivern and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated at the end

import pytest
@pytest.mark.smoke
def test_firstProgram():
     print("Hello")

@pytest.mark.xfail
def test_SecondCriditCard():
     print("Good Morning")

#def test_crossBrowser(crossBrowser):
 #    print(crossBrowser)

