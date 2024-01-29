# try:
#     #a=10
#     #print(a)
#    # print(a + 10)
#     print(1 / 0)
# #except Exception as var:
#  #   print(var)
#   #  print("error handling")
# except Exception as NameError:
#     print("NameError error caught")
# #except Exception as TypeError:
#  #   print("TypeError error caught")
# except Exception as ZeroDivisionError:
#      print("ZeroDivisionError handled")
#      #print(var)
#
# else:
#    print("Not handling error")
# finally:
#    print("Printing final block")
#
# #raise Exception("exception caught")
#raise Exception("TypeError")

# a=-12
# if a>0 and a<100:
#     print("Valid")
# else:
#     raise AssertionError("Invalid")

# if n>0 and n<110:
#     print("valid age")
# else:
#     raise AssertionError("invalid age")
# n=-112
# assert n>0 and n<110, ("invalid age")


# n=-12
# try:
#
#     if n>0 and n<110:
#         print("valid age")
#     else:
#         raise AssertionError("invalid age")
#
# #except Exception as msg:
# except AssertionError as msg:
#     print("exception happened", msg)
#
# else:
#     print("no error happened")
#
# finally:
#     print("finnaly block executed")

n=12
try:
    print("Valid")
    assert n>0 and n<110, ("invalid age")

#except Exception as msg:
except AssertionError as msg:
    print("exception happened", msg)