#non keyword arguments

def myFun(arg2, *argv):
    print ("First argument :", arg2)
    
    for arg in argv:
        print("Next argument through *argv :", arg)
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


