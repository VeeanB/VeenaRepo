import pytest


@pytest.mark.usefixtures("setup1")
class Test:


    def test_fixtureDemo(self):
         print("i will execute steps in fixtureDemo methods")

