numbers = []
num = int(input("Enter the number of elements: "))
if num<=0:
    print("atleast give one input")
else:
 for i in range(0, num):
    element = int(input("Enter the element: "))
    numbers.append(element)

result = filter(lambda x: x > 4 and len(str(x)) > 0, numbers)
print("The elements having length greater than 0 and greater than 4 are: ", list(result))