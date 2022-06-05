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

