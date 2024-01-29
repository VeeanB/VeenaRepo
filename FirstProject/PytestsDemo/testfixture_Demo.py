import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

     def test_fixtureDemo(self):
          print("i will execute steps in fixtureDemo methods")

     def test_fixtureDemo1(self):
          print("i will execute steps in fixtureDemo1 methods")

     def test_fixtureDemo2(self):
          print("i will execute steps in fixtureDemo2 methods")

     def test_fixtureDemo3(self):
          print("i will execute steps in fixtureDemo3 methods")