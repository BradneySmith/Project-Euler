def find_factor(num):
  factor = 2
  while factor * factor < num:
       while num % factor == 0:
           num = num / factor
       factor+= 1
  return num
  
  print(find_factor(600851475143))