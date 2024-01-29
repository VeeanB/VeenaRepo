import pytest


@pytest.fixture(scope="class")
def setup1():
     print("I will be executing first")
     yield
     print("I will executed last")



