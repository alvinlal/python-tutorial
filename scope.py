'''
LEGB 
local, Enclosing, Global, Built-in
'''

x = 'global x'


def test():
    y = 'local y'  # local variable
    x = 'local x'
    print(x)
    print(y)


# print(y) error

test()
print(x)


def test_2():
    global x  # changes global x variable , create an x variable in the global scope even if it doesn't already exist in the global scope
    x = 'local x'
    print(x)


print('---------')  # print is in built-in scope

test_2()
print(x)


print('---------')


def outer():
    s = 'outer s'  # enclosing scope of inner()

    def inner():
        s = 'inner s'
        print(s)

    inner()
    print(s)


outer()

print('---------')


def outer():
    s = 'outer s'

    def inner():
        nonlocal s  # s is now of enclosing scope
        s = 'inner s'
        print(s)

    inner()
    print(s)


outer()
