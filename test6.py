
def getInfo():
    var1 = input("\nplease provide the first numeric value: ")
    var2 = input("\nplease provide the second numeric value: ")
    return var1,var2

def compute():
    go = True
    while go:
          var1,var2 = getInfo()
          try:
             var3 = int(var1) + int(var2)
             go = False
          except ValueError as e:
                print("{}: \n\nYou did not provide a numerci value".format(e))
          except:
                print(" \n\nOops, you din't provide what was needed")
    print("{} + {} = {}".format(var1,var2,var3))
       

if __name__== "__main__":
    compute()
