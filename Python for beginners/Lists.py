# list is an ordered mutable collection of items

prices = [40, 30, 20 , 53]
print(prices)

print(prices[0])
print(prices[3]) # +ve indexing

print(prices[-1])
print(prices[-4]) # -ve indexing

print(prices[1:3])
print(prices[:-1:-1]) # slicing a list

prices[2] = 45 # updating

prices.append(50) # adding elements
prices.extend([50, 60])
prices.insert(1, 15)

prices.pop() # removing elements
prices.remove(30)
prices.clear() # remove all the elements

