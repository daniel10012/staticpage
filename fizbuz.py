def fizzbuzz(number):
  # if the number is divisible by 3 outpout Fizz
  # if the number is divisible by 5 outpout Buzz
  # if the number is divisible by 3 and 5 outpout FizzBuzz
  # Each result should be printed e.g starting at 1 until number(15)
  # Fizz for 3
  # Buzz for 5
  # Fizz for 6
  # Fizz for 9
  # Buzz for 10
  # Fizz for 12
  # FizzBuzz for 15
    f =""
    b = ""
    if number % 3 == 0:
        f = "Fizz"
    if number % 5 ==0:
        b = "Buzz"

    for num in range(1,number+1):

        f = ""
        b = ""
        if num % 3 == 0:
            f = "Fizz"
        if num % 5 == 0:
            b = "Buzz"
        if (f + b) != "":
            print (f"{f + b} for {num}")




fizzbuzz(1000)

