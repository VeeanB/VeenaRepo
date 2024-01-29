#Any pytest file should start with test_
#Any Pytest method should start with test_
#Any code should be wraped in method only
import pytest

@pytest.mark.smoke
@pytest.mark.skip

def test_firstProgram():
     msg = "Hello"
     assert msg == "Hi" ,"Test failed becuase stings do not match"


def test_SecondCriditCard():
     a = 4
     b = 6
     assert a+2 == 6 ,"Addition do not match"
