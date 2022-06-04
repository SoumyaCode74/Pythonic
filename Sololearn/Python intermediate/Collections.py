'''
For Python Data structures
'''
print('='*10,'Dictionaries','='*10)
pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

print('-'*20)

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

# country = input("Enter the country's name: ")
country = 'Canada'
print("%s's economic rank is: %s" % (country, data.get(country, 'Not found')))


print('='*10,'Tuples','='*10)

my_tuple = "one", "two", "three"
print(my_tuple)
print('-'*20)
numbers = 1, 2, 3
a,b,c = numbers
print("The set of numbers is: ", numbers)
print("Before swapping: a=%d, b=%d" % (a,b))
a,b = b,a
print("After swapping: a=%d, b=%d" % (a,b))
print('-'*20)
a, b = [6, 8]
print("Before swapping: a=%d, b=%d" % (a,b))
a,b = b,a
print("After swapping: a=%d, b=%d" % (a,b))
print('-'*20)
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
print('-'*20)
a, b, c, d, *e, f, g = range(20)
print(e,'\n',len(e))

print('='*10,'Sets','='*10)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
num = 3
print("Is %d in the set? %s" % (num,("Yes" if num in nums else "No")))
nums.add(-7)
nums.remove(3)
print(nums)
print("Is %d in the set? %s" % (num,("Yes" if num in nums else "No")))
print('-'*20)
print('Set operations')
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print("Union = ", first | second)
print("Intersection = ", first & second)
print("first - second = ", first - second)
print("second - first = ", second - first)
print("symmetric difference = ", first ^ second)
print('-'*20)
skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
print(f"Matched skill is {(skills & job_skills).pop()}")

print('='*10,'List comprehension','='*10)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
print('-'*20)
word = 'awesome'
letters = list(word)
print([x for x in letters if x not in {'a','e','i','o','u'}])
