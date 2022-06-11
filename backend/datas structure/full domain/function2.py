def func2(text):
    return text.upper() 

def func3(text):
    return text.lower()



def func1(func):
    result = func('Hello world')
    print(result)


func1(func2)

