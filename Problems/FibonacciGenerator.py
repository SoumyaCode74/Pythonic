print("""
In this problem, the objective is to print the list of fibonacci numbers between two specified numbers

Sample input
Enter the start value 1
Enter the last value 3

Sample output
The list of fibonacci numbers from 1 to 3 is: [1,2,3]
""")

def fibonacci(num):
    if num < 0:
        num = -num
    elif num <= 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci_series(start, end):
    for i in range(start, end+1):
        yield fibonacci(i)

if __name__ == "__main__":
    start = int(input("Enter the start value: "))
    end = int(input("Enter the last value: "))
    print(f"The list of fibonacci numbers from {start} to {end} is: ", list(fibonacci_series(start, end)))
