def factorial(n)
    if n== 0:
        return 1
    else:
         return n * factorail(n-1)
number = 5
result = factorial(number)
print(f"the factorail or {number} is {result}.")
