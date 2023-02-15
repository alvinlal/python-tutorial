def hello_func():
    print('hello function!')


hello_func()


def hello_func():
    return 'hello function'


print(hello_func())


def sum(a, b):
    return a+b


print(sum(2, 1))


def greet(greeting='good morning'):
    return f"hi, {greeting}"


print(greet())


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
