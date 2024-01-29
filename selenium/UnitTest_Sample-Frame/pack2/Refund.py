import unittest
class TestRefund(unittest.TestCase):
   def test_refundinbank(self):
        print("Refund in bank finished")
   def test_refundinwallet(self):
        print("Refund in wallet finished")
   if __name__ == "__main__":
      unittest.main()