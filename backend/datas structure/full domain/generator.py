# A simple generator function
class hello:
    def my_gen():
        n = 3
        print('This is printed first')
        # Generator function contains yield statements
        yield n
        yield n

        n = 100
        print('This is printed second')
        yield n

        n = 2
        print('This is printed at last')
        yield n


# a =my_gen()

# next(a)
# next(a)
# next(a)

for item in hello.my_gen():
    print(item)
