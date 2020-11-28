'''Contain functions for generating fibonacci numbers.'''
     
def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n == 1:
        return 1
    else:
        return 0

def fibonacci_iteration(n):
    '''Returns the Fibonacci number of order n but without recursion.'''
    if n > 1:
        _, F = 0, 1
        while n > 1:
            _, F, n = F, F + _, n - 1
        return F
    elif n == 1:
        return 1
    else:
        return 0
