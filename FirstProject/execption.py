ItemsIncart = 0
# 2 items to added to cart
if ItemsIncart != 2:
    pass

    assert (ItemsIncart == 0)


     #raise Exception("Product count not matches 2")

#try , catch

try:
    with open('test.txt','r') as reader:
         reader.read()

except Exception as e:  #execute only when try failes
    print(e)
    #print("Some how i reached this blocked its failure in try block")
finally: #executed every time with failure or nor
    print("cleaning up resources")
