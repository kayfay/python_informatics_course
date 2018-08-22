value = input("Please provide me with a number higher than a single digit: ex. 01 or 67 ")
sum = 0
for i in list(str(value)):
              sum += int(i)
print(sum)    
