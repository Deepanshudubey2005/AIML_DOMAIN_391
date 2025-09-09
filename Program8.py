a=int(input("Enter the number :"))
fact=1
for i in range (a,0,-1):
    fact=fact*i
    
print("Factorial is",fact)
fact=1
while a>0 :
    fact=fact*a
    a=a-1
print("Factorial is",fact)    

