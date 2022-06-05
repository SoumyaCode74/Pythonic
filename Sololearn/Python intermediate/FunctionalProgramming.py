'''
Python functional programming
Functional: function of functions
'''
stars = '*'*10
dashes = '-'*10
print('Introduction',stars)
def apply_twice(func, arg):
    return func(func(arg))

def square_function(x):
    return x**2

print(apply_twice(square_function,10))
print('Pure and impure functions',dashes)
#Pure function
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)        #Depends wholly on function arguments
some_list = []
#impure function
def impure_function(arg):
    return some_list.append(arg) #Depends on variables outside function scope

print("Pure function result: ", pure_function(10,20))
impure_function(10)
print("Impure function result: ", some_list)

print('Lambdas',stars)
def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))
print(dashes)
#named function
def polynomial(x,y):
    return x**2 + 5*y + 4
print("Through conventional definition: ", polynomial(-4,2))

#lambda
print("Through anonymous function", (lambda x,y: x**2 + 5*y + 4) (-4,2))
print("Maps & Filters",stars)
print("Maps")
#Maps : function that makes a function operate on each item of an iterable and return a new iterable
print("without using map functional", dashes)
def add_two_numbers(x,y):
    return x+y
nums1 = range(1,10)
nums2 = range(10,20)
new_nums = list()
for i in range(len(nums1)):
    new_nums.append(add_two_numbers(nums1[i], nums2[i]))
print("List of added numbers: ", new_nums)
print("with using map functional", dashes)
new_nums = []
new_nums = list(map(lambda x,y:x+y, nums1,nums2))
print("List of added numbers: ", new_nums)
print(dashes)
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = 10
salaries = list(map(lambda salary: salary * (1+0.01*bonus), salaries))
print("Incremented salary list with 10% bonus", salaries)
print(dashes*3)
print("Filters")
#filter: same as map only returns a "filtered"
# list of objects from the passed on iterable that satisfies the condition
nums = list(range(1,30))
nums_odd = list(filter(lambda x: x%2 != 0, nums))
nums_even = list(filter(lambda x: x%2 == 0, nums))
print("List of numbers", nums)
print("List of odd numbers", nums_odd)
print("List of even numbers", nums_even)
print(dashes*3)
print("Generators")
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
print(dashes)
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
print(dashes*3)
print("Decorators")
#Decorators: Decorators provide a way to modify functions using other functions.
#This is ideal when you need to extend the functionality of functions that you don't want to modify.
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)
print_text()
print(dashes)
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()
print(dashes*2)
def decor(func):
    def wrap(arg):
        print('*'*3)
        func(arg)
        print('*'*3)
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice('225')

def heading_decor(func):
    def wrap(msg):
        print('*'*10,end = " ")
        func(msg)
        print('*'*10)
    return wrap

def subheading_decor(func):
    def wrap(msg):
        print('-'*10,end = " ")
        func(msg)
        print('-'*10)
    return wrap


@heading_decor
def print_heading(heading):
    print(heading, end = " ")

@subheading_decor
def print_subheading(subheading):
    print(subheading, end=" ")

print_heading("Using decorated headings")

print_heading("Variable args and named args")
print_subheading("Minimum number")


def my_min(*args):
    minimum = args[0]
    for i in range(1, len(args)):
        if args[i] < minimum:
            minimum = args[i]
    return minimum

print("The minimum value is: ", my_min(8, 13, 4, 42, 120, 7))

