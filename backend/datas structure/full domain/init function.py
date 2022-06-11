class hello:
    def __init__(self,var):
        self.var=var
        print('constructor is called ')
        print(self.var)
    def display(self,word):
        self.var=word
        print('display is called',self.var)




a = hello("miras")

a.display('wafi')

