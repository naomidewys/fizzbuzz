logo = '''
  __ _         _                   
 / _(_)_______| |__  _   _ ________
| |_| |_  /_  / '_ \| | | |_  /_  /
|  _| |/ / / /| |_) | |_| |/ / / / 
|_| |_/___/___|_.__/ \__,_/___/___|
'''

print(logo)
print("Let's play a game of FizzBuzz!")
print("Numbers divisible by 3 will be 'Fizz', by 5 will be 'Buzz', and by 15 will be 'FizzBuzz'.")
print("Choose two numbers to get started:")
number1 = int(input("What is your first number?\n"))
number2 = int(input("What is your second number?\n"))

for number in range(number1, number2 + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)