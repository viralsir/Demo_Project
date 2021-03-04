''' display sum of given 5 no.  '''
'''
  use loop and list 
'''
list = []
for i in range(5):
    list.append(int(input("Enter Number: ")))
print(list)
print("Sum of 5 Numbers is:  ", sum(list))