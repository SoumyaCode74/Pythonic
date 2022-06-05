print("""
Decimal to Binary:
Sample Input
8

Sample Output
1000
""")

def convert(num):
   if num == 1:
      return num
   else:
      return (num % 2 + 10 * convert(num // 2))
num = int(input("Enter a decimal number: "))
print(convert(num))