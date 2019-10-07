# if the number is multiply of 3 return "fizz". If it is multiple of five return "Buzz" 
# if the number is mutliple both five and three then return "fizzBuzz"


def fizzBuzz(n):
    result=[]
    for i in range(1, n+1):
        if i % 3==0:
            result.append("Fizz")
        elif i % 5==0:
            result.append("Buzz")
        elif i % 15==0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))
    return result 








print(fizzBuzz(100))
