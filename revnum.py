a = int(input())    
b = 0    
while(a > 0):    
    Reminder = a %10    
    b = (b *10) + Reminder    
    a = a //10    
print(b)
