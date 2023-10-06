i=2
while i >=0:
    print("*")
    i-=2
print()
for i in range (-1,1):
    print("#")
print()
z=10
y=0
x=z>y or z==y
print(x)
print()
my_list=[3,1,-1]
my_list[-1]=my_list[-2]
print(my_list)
print()
vals=[0,1,2]
vals[0], vals[1]=vals[1], vals[2]
print(vals)
print()
nums=[]
vals=nums
vals.append(1)
print(vals)
print()
my_list=[0 for i in range(1,3)]
print(my_list)
print()
my_list =[0,1,2,3]
x=1
for elem in my_list:
    x*=elem
print(x)