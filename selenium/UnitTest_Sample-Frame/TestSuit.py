import unittest
from pack1.Login import Testlogin
from  pack1.Signup import TestSignup
from pack2.Transfer import TestPayment
from pack2.Refund import TestRefund


tc1=unittest.TestLoader().loadTestsFromTestCase(Testlogin)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestSignup)
tc3=unittest.TestLoader().loadTestsFromTestCase(TestPayment)
tc4=unittest.TestLoader().loadTestsFromTestCase(TestRefund)

master = unittest.TestSuite([tc1, tc2, tc3,tc4])
sanity = unittest.TestSuite([tc1, tc2])
func = unittest.TestSuite([tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(sanity)




#regular expression module
#Lamnda functions
#run() and Popen() functions
#python suitable for which type of applications server -side or client side
#PYTHONPATH ,PYTHONSTARTUP,PYTHONCASEOK
#a=”pythontutorial”
#print(‘%. 6s’ % a)
#match’ and ‘search’
#pickling and unpickling
#generators
#QR Code and barcode,Image capture
