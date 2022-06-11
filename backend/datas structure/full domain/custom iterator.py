class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max-1

    def __iter__(self):
        self.n = 0
        self.test="working bro"
       
        print('iterator turned on')
        return self

    def __next__(self):
        
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            # print(thg.test)
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(10)


# create an iterable from the object

i = iter(numbers)


# Using next to get to the next iterator element

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

