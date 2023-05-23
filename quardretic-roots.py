from cmath import sqrt


a=int(input('enter the co-efficent of highest order \n'))
b=int(input('enter the co-efficent of 2nd highest order \n'))
c=int(input('enter the constant \n'))
d=b*b-4*a*c
if(d>0):
  root1= (-b+sqrt(d))/2*a
  root2= (-b+sqrt(d))/2*a
  print(root1,root2,'are the roots of the quaratic equation')
elif(d==0):
  root3 = -b/2*a
  print('this equation have equal roots i.e.',root3)
else:
  print('real root doesn\'t exist')