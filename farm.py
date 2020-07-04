money = 1296
prices = {'chicken': 23, 'goat': 678, 'pig': 1296, 'cow': 3848, 'sheep': 6769}
can_afford = []
for animal in prices.keys():
    if money // prices[animal] > 0:

        can_afford.append((money // prices[animal], animal))
# print the highest value and key of that value
# {value} {key}
if can_afford != []:
    if can_afford[-1][0] == 1 or can_afford[-1][1] == 'sheep':
        print(can_afford[-1][0], can_afford[-1][1])
    else:
        print(can_afford[-1][0], can_afford[-1][1] + 's')
else:
    print('None')
