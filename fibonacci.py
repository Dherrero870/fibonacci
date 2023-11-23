# Paso 2
def fib_naive(n, allNumbers = {}):
    if n in allNumbers[n]
        return allNumbers[n]
    if n <= 1:
        return n
    else:
        return fib_naive(n-1) + fib_naive(n-2)
"""
print (fib_naive(5))
print (fib_naive(6))
"""
# Paso 3
allNumbers = {}
while True:
    numero = int (input("¿Qué numero quieres calcular?"))
    print (fib_naive(numero))
# Paso 4
def fib_memo(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
"""
print(fib_memo(5))
print(fib_memo(6))
"""
# Paso 5
import time
start_time = time.time()
result_naive = fib_naive(30)
end_time = time.time()
print(f"Naive approach result: {result_naive}")
print(f"Naive approach execution time: {end_time - start_time} seconds")
start_time = time.time()
result_memo = fib_memo(30)
end_time = time.time()
print(f"Memoization approach result: {result_memo}")
print(f"Memoization approach execution time: {end_time - start_time} seconds")