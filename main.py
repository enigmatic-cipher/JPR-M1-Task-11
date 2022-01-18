"""
Given n as input, print the following pattern. Note that all the multiples of 3 have been denoted by x.
Input-> n=4
Output-> 
4 
4x 
4x2 
4x21
"""

n = 4
st = ""
pt = "x"
for i in range(1,n+1):
  if(n%3==0):
    st = st + pt
  else:
    st = st + str(n)
  n = n-1
  print(st)
