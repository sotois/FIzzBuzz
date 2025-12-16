def check_fizzbuzz(number):
  if number % 3 == 0 and number % 5 == 0:
    return "Fizz-Buzz"
  
  elif number % 3 == 0:
    return "Fizz"
    
  elif number % 5 == 0:
      return "Buzz"
    
  else:
    return str(number)
    
def play_fizzbuzz():
  i = 1
  while i <= 100:
    print(check_fizzbuzz(i))
    i += 1
    
play_fizzbuzz()
