# To find given number is armstrong or not
a=int(input("Enter the number :"))
sum=0
d=a
o=len(str(a))
while (d>0) :
    c=d%10
    e=pow(c,o)
    sum=sum+e
    d=d//10
if (sum==a) :
    print("Entered number is armstrong")
else :
    print("Entered number is not armstrong")   


