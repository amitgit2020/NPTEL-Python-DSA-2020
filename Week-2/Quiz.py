# 1) One of the following 10 statements generates an error. Which one? (Your answer should be a number between 1 and 10.)

x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
y = x[0:50]                          # Statement 2, Makes new list 
z = y                                # Statement 3, pointing to y
w = x                                # Statement 4
x[0] = x[0][:5] + 'ery'              # Statement 5
y[2] = 4                             # Statement 6
z[4] = 42                            # Statement 7
w[0][:3] = 'fea'                     # Statement 8 , generates an error
x[1][0] = 5555                       # Statement 9
a = (x[4][1] == 1)                   # Statement 10, TypeError: 'int' object is not subscriptable


# 2) Consider the following lines of Python code.
'''
Which of the following holds at the end of this code?
 a[1] == 77, b[2] == 77, c[2] == 77, d[0] == 97
 a[1] == 87, b[2] == 87, c[2] == 77, d[0] == 97
 a[1] == 87, b[2] == 77, c[2] == 77, d[0] == 97
 a[1] == 97, b[2] == 77, c[2] == 77, d[0] == 97 
'''

b = [23,44,87,100]
a = b[1:]
d = b[2:]
c = b
d[0] = 97
c[2] = 77

# Sol-c

# 3) What is the value of endmsg after executing the following lines?

startmsg = "python"
endmsg = ""
for i in range(1,1+len(startmsg)):
  endmsg = startmsg[-i] + endmsg


# Sol- "python"


# 4) What is the value of mylist after the following lines are executed?

def mystery(l):
  l = l[1:]
  return()

mylist = [7,11,13]
mystery(mylist)

# Sol -[7,11,13]
# The update l = l[1:] inside the function creates a new list, so the list passed as the argument is not changed.
