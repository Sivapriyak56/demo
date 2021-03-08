f=open("sa.txt","r")
f1=open("ma.txt","w")

count=0
for x in f:
    count+=1
    if(count%2!=0):
        f1.write(x)
f1 = open("ma.txt", "r")
print(f1.read())


