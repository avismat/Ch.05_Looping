'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''

import random

headsCount = 0
tailsCount = 0
totalHeads = [0] * 100



headsCount = 0
tailsCount = 0
for i in range(50):
    coinFlip = random.randint(0,1)
    headsCount += 1 if coinFlip == 1 else 0
    tailsCount += 1 if coinFlip == 0 else 0
    totalHeads[i] = headsCount

print("Heads count: {}\nTails count: {}".format(headsCount,tailsCount))
print("Total: {}".format(headsCount + tailsCount))












