a=int(input())
b=1
if a<21:
  if a==1:
    print('1')
  else:
    for i in range(1,a+1):
      b=b*i
    print(b)
