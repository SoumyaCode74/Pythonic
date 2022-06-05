print("""
Spelling Backwards:
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
""")
def spell(txt):
    #your code goes here
    if len(txt) == 1:
        print(txt)
    else:
        characters = list(txt)
        length = len(characters)
        print(characters[-1])
        spell(''.join(characters[:length-1]))


txt = input("Enter the text to spell backwards: ")
spell(txt)