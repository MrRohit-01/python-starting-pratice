a=int(input("enter first number"))
b=int(input("enter second number"))
for i in range(1,max(a+1,b+1)):
  if (a%i==0 and b%i==0):
    hcf=i

for j in range(1,a*b+1):
  if (a%j==0 and b%j==0):
    lcm=i
    break
print(hcf,'is the gcd of',a,'and' ,b, )
print(lcm,'is the lcm of',a,'and' ,b, )