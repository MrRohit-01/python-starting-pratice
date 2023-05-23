a=int(input('enter a number for checking armstrong or not'))
x=a
y=a
count=0
sum=0
while(x!=0):
  x=int(x/10)
  count+=1
print(count)
while(y!=0):
  rem=y%10
  y=int(y/10)
  sum=sum + (rem**count)
print(sum)
if(sum==a):
  print('this is a armstrong number')
else:
  print('this is not a armstrong number')