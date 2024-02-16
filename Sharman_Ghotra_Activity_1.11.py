# Ice cream prices
prices = {'Chocolate':5, 'Vanilla':4, 'Strawberry':7, 'Cookie':8}  # Defines list

print('\nFlavors include -')
for flavor in prices:
    print(flavor)  # Returns the "flavor" of the list, the variable name(s)

print('\nPrices per Flavor -')
for flavor,cost in prices.items():  # Splits the list into two parts, flavors and cost are defined
    print(f'{flavor} | ${cost}')

print('\nCost for Extra Sprinkes :')
for num in range(10, 0, -1):
    print(f'{num} TSP - ${num * 3}')  # Loops from 10 to 1 with a -1 jump, multiplies by 3 to determine cost

