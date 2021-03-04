''' display the factorial of given no'''
a = int(input("Enter a number:"))
fact = 1
if a < 0:
    print("not possible")
elif a == 0:
    print("fact is 1")
else:
    for i in range (1, a+1):
        fact = fact * i
print("The factorial of", a, "is", fact)


