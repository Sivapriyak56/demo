y1=int(input("enter the current year:"))
y2=int(input("enter the last year:"))
for i in range(y1,y2+1):
    if(i%4==0 or i%100==0 or i%400==0):
        print(i)