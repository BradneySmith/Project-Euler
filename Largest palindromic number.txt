def palindrome_check(num):
  return str(num) == str(num)[::-1]

def get_largest_palindrome(min, max):
  largest_palindrome = 0
  for b in range(min, max):
    for a in range(min, max):
      if (palindrome_check(a*b) == True) and (a*b > largest_palindrome):
        largest_palindrome = a*b
        print("a is {}, b is {}, a*b is {}".format(a,b,a*b))

  print(largest_palindrome)
  
get_largest_palindrome(100,999)