string=input("Enter string:")
a=[]
count=3
a=string.split(" ")
for i in range(0,len(a)):
      if(count==a[i]):
            count=count+1
print("repeatd words are:")
print(a[i])
