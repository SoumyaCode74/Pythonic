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