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
  for i in range(1, 101):
    print(check_fizzbuzz(i))
    
play_fizzbuzz()
