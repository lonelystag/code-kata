#this code is to find the given num is an expo value of 2
a=int(input())
def isPowerOfTwo (x):
  return (x and (not(x & (x - 1))) ) 
  # Driver code 
if(isPowerOfTwo(a)): 
    print('yes') 
else: 
    print('no') 
