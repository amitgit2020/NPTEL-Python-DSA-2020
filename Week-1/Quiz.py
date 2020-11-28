def h(x):
    (d,n) = (1,0)
    while d <= x:
        (d,n) = (d*3,n+1)
    return(n)


def g(n): 
    s=0
    for i in range(2,n):
        if n%i == 0:
           s = s+1
    return(s)


def f(n): 
    s=0
    for i in range(1,n+1):
        if n//i == i and n%i == 0:
           s = 1
    return(s%2 == 1)


def foo(m):
    if m == 0:
      return(0)
    else:
      return(m+foo(m-1))
      

'''
1) What does h(19685) return for the following function definition?
2) What is g(36) - g(35), given the definition of g below?
3) The function f(n) given above returns True for a positive number n if and only if:
    n is an odd number.
    n is a prime number.
    n is a perfect square.
    n is a composite number.
4) Which of the following is correct?
    The function always terminates with f(n) = factorial of n
    The function always terminates with f(n) = n(n+1)/2
    The function terminates for non­negative n with f(n) = factorial of n
    The function terminates for non­negative n with f(n) = n(n+1)/2
'''


# Sol-10
# Sol-5
# f(n) sets s to 1 if there is a number i such that i*i == n. n is a perfect square.
# If m is negative, the function does not terminate. Otherwise, it computes 1+2+..+m = m(m+1)/2.