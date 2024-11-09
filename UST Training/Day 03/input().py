print("Hello, what is your number")
input=input()
print("My number is ", input)

def oddOreven(input):
    if int(input)%2==0:
        return "even"
    else:
        return "odd"
print(oddOreven(input))