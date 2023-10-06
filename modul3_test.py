my_list=[1,2,3]
for v in range(len(my_list)):
    my_list.insert(1,my_list[v])
print(my_list)

print()

my_list_b=[i for i in range(-1, 2)]
print(my_list_b)

print()

nums=[1,2,3]
vals=nums
del vals[1:2]
print(nums)
print(vals)

print()

my_list_c=[1,2,3,4]
print(my_list_c[-3:-2])

print()

valsb=[0,1,2]
valsb.insert(0,1)
del valsb[1]
print(valsb)

print()

#my_list_d=[[0,1,2,3] for i in range(2)]
#print(my_list_d[2][0])

print()
nums=[1,2,3]
vals=nums[-1:-2]
print(nums)
print(vals)

print()

i=0
while i <=3:
    i +=2
    print("*")

print()
my_list_e=[3,1,-2]
print(my_list_e[my_list_e[-1]])

print()
for i in range(1):
    print("#")
else:
    print("#")


print()
t=[[3-i for i in range(3)] for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
print(s)

print()
#a=1
#b=0
#c=a&b
#d=a
#e=
#NEM 3
print()

#x=1
#print(x=x==x)
print()
#z=10
#y=0
#print(x=y<z and z>y or y>z and z<y)
print()
#var = 1#NEM 0
#while var < 10:
#    print("#")
#    var = var << 1
#NEM 1

print()
vals=[0,1,2]
vals[0], vals[2]=vals[2], vals[0]
print(vals)

print("17/20")
egy=[1,2,3]
ketto=[]
for v in egy:
    ketto.insert(0,v)
print(ketto)
print()
i=0
while i<=5 :
    i +=1
    if i % 2 == 0:
        break
    print("*") #1ncsillag

print()
var=0
while var <6:
    var +=1
    if var %2==0:
        continue
    print("#") #3
print()
print("==")