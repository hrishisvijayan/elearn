def div(a,b):
    print('normal function is called')
    print(a/b)

def smart_div(func):
    print('smart div first layer')
    def inner(c,d):
        print('inner function is called')            
        if c<d:
            c,d=d,c
        return func(c,d) 
    return inner
 





div = smart_div(div)

div(2,4)
