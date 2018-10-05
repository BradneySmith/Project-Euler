LIMIT = 1000 #Limit is exclusive
sum = 0 #Stores the value of the sum of all multiples
for x in range (LIMIT):
  if (x%3 == 0) or (x%5 == 0): sum+= x
print(sum)