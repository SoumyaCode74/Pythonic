print("""
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.

Sample Input
hello

Sample Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
""")
print('*'*5, "Solution (using Python generator)", '*'*5)
text = "Python is awesome"
print(f"Input text: {text}")
counter = dict()
character_set = set()
#your code goes here
def character_list(word):
    for ch in list(word):
      if ch != ' ':
        yield ch
      else:
        continue
#When the generator yields 1 item, it holds on until the outer for-loop
#calls the next() function on it, then the generator yields the next item

for character in character_list(text):
    if character not in counter.keys():
        counter[character] = 1
    else:
        counter[character] += 1

print("Character count: ", counter)