  #Sign your name: Matthew

import random

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
start = 2
stop = 100
step = 2
for i in range(start,stop+1,step):
    print(i)

print("------------")


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while i >= 0:
    print(i)
    i -= 1

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
print("Your random number is {}".format(random.randint(1,10)))





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
numberList = [0,0,0,0,0,0,0]

def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum

def num_type_list(l):
    types = [0,0,0]  # Positives, zeroes, negatives
    for i in l:
        if i > 0:
            types[0] += 1
        elif i < 0:
            types[2] += 1
        else:
            types[1] += 1

    return types

for i in range(7):
    num = int(input("Number #{}: ".format(i+1)))
    numberList[i] = num

print("The sum of your list is {}".format(sum_list(numberList)))
print("{} Positives".format(num_type_list(numberList)[0]))
print("{} Zeroes".format(num_type_list(numberList)[1]))
print("{} Negatives".format(num_type_list(numberList)[2]))

