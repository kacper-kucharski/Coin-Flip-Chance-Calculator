import random

amount = int(input('Enter how many simulations should be run: '))

heads = 0
tails = 0

for x in range(amount):
    num = random.randint(0,1)
    if num == 0:
        heads += 1
    elif num == 1:
        tails += 1

print('Chance to get heads is',str(round(heads/amount * 100, 2)) + '%')
print('Chance to get tails is',str(round(tails/amount * 100, 2)) + '%')
