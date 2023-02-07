my_str="Hello this is an Example with cased letters"

my_str=input("Enter a string:")

words=[word.lower() for word in my_str.split()]

words.sort()

print("The sortedwords are:")
for word in words:
    print(word)
