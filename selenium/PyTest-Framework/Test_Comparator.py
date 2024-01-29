import pytest

class TestComp:
  @pytest.mark.skip(reason='Skipped test case')
  def test_equal(self,start3):
    #print("Equal function is executing")
    assert 3==3

  #@pytest.mark.skipif(5>4,reason="No need to exexute")
  @pytest.mark.functionality
  def test_greater(self,start2):
    #print("greater function is executing")
    assert 5>4

  @pytest.mark.xfail(reason='no needed output')
  @pytest.mark.parametrize('name',['name1','name2','name3'])
  @pytest.mark.parametrize(('a','b'),[(2,3),(4,5),(3,6)])
  @pytest.mark.regression
  def test_less(self,start4,name,a,b):
    #print("less function is executing")
    assert 4>5

