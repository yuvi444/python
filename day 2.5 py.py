a=int(input("enter the no of list :"))
b=[]
for i in range(0,a):
   c=int(input("enter the value :"))
   b.append(c)
d=int(input("enter the no of list :"))
e=[]
for i in range(0,d):
   f=int(input("enter the value :"))
   e.append(f)
g=[]
g=b+e
g.sort()
print(g)
