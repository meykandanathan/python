numbers = input("Enter a list of numbers separated by space: ").split()
if numbers<=0:
    print("alteast 1 input")
else:
  result = list(filter(lambda x: len(x)>0 and int(x)>4, numbers))

print("Numbers having length greater than 0 and greater than 4:", result)