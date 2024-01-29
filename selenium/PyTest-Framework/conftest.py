import pytest
@pytest.fixture()
def start1():
    print("Starting setup1")
    yield True,True
    print("teardown method 1")

@pytest.fixture()
def start2():
    print("Starting setup2")
    yield True,True
    print("teardown method 2")

@pytest.fixture(scope='class')
def start3():
    print("this is setup 3")
    yield
    print("this is teardown`3")

@pytest.fixture(scope='module')
def start4():
    print("this is setup 4")
    yield
    print("this is teardown`4")

def pytest_configure(config):
    config.addinivalue_line("markers", "functionality: functional testing")
    config.addinivalue_line("markers", "regression: regression testing")