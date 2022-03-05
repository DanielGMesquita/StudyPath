def fizzbuzz(x):
    if x % 3 == 0 and x % 5 != 0:
        r = 'Fizz'
    elif x % 3 != 0 and x % 5 ==0:
        r = 'Buzz'
    elif x % 3 == 0 and x % 5 ==0:
        r = 'FizzBuzz'
    else:
        r = x
    return r