'''
1) A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.
>>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True
'''
# def primeproduct(m):
#     l=[]    
#     if m>=2:
#         for i in range(2,m):
#             if m%i==0:                
#                 l+=[i]            
#         if len(l)==2:
#             if m==l[0]*l[1]:
#                 if l[1]%l[0]==0:
#                     return False
#                 return True
#         elif len(l)==1:
#             if m==l[0]*l[0]:
#                 return True
#         else:
#             return False     
#     else:
#         return False

def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist.append(i)
    return(factorlist)

def isprime(n):
    return(factors(n) == [1,n])

def primeproduct(n):
    for i in range(1,n+1):
        if n%i == 0:
            if isprime(i) and isprime(n//i):
                return(True)
    return(False)

'''
2) Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

Here are some examples to show how your function should work.

 
>>> delchar("banana","b")
'anana'

>>> delchar("banana","a")
'bnn'

>>> delchar("banana","n")
'baaa'

>>> delchar("banana","an")
'banana'
'''

def delchar(s,c):
    if len(c) != 1:
        return(s)
    snew = ""
    for char in s:
        if char != c:
            snew = snew + char
    return(snew)

'''
3) Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first elment in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.

>>> shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]

>>> shuffle([0,2,4],[1])
[0, 1, 2, 4]

>>> shuffle([0],[1,3,5])
[0, 1, 3, 5]
'''
def shuffle(l1,l2):
    if len(l1) < len(l2):
        minlength = len(l1)
    else:
        minlength = len(l2)
    shuffled = []
    for i in range(minlength):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    shuffled = shuffled + l1[minlength:] + l2[minlength:]
    return(shuffled)