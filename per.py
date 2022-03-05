import enum
from ssl import enum_certificates


def mydec(f):
    def wrapper(a,b):
        a= a.capitalize()
        b= b.capitalize()
        return f(a, b)
    return wrapper

@mydec
def printnm(name1, name2):
    # return name 1, name2
    print("Hello {} Hello {}".format(name1,name2))
# def printnm(a,b,c):
#     print("ankit",a,b,c)

name1 = "andrea"
name2 = "ponting"
printnm(name1, name2)
# O/P:
# output => 'Hello Andrea! Hello Ponting!'

str_ = "ABCDEFGHIJKLMNOPQRSTUVWX"
# O/P:
# ABCD
# EFGH
# IJKL
# MNOP
# QRST
# # UVWX
p = 0
# print("STR_",str_)
for t in range(0,len(str_),4):
    print("STR_",str_[t:t+4])
#     if t%4==0:
#         # p = t
    
#         # print(p,t)
    # p= t

# Given a list of n unique positive and negative number
f = [2,4,1,6,9,18,89,11,89]
numbers = f
# Given k , find the first 2 numbers which has sum=k
k = 100
g = f[0]
rangf = range(len(f))
rangfy = range(1,len(f))
# d = list(filter(lambda x,y:f[x]+f[y]==k, (rangf, rangfy)))
# print("sum--------------g", range, enumerate(f))
for y in range(1,len(f)):
    if g+f[y]==k:
        print("sum--------------g, f[y]",g,f[y])
        break
    g= f[y]
    # for j in range(y+1,len(f))
print([x for x in zip(f,f) if sum(x)==k])
# d = lambda x,y:x+y
# print("sum--------------",list(map(sum , [1,2,3,4])))
# result = d(*f)
# t -= f
r = f[0]
for t in f[1:]:
    if r+t==k:
        print(r,t)
# print("result",result)
target = k
for x in numbers:
    for y in numbers:
        # print("target12",x,y)
        if x+y==target:
            print("target",x,y)
from functools import reduce
print(list(filter(lambda x:x+x==k,f)))
d = lambda x,y:x+y==k
# print("value",d(f,f))
from itertools import combinations, permutations
# for t in range(2,len(f)):
d = combinations(f,2)
for y in d:
        # print(y, sum(y))
    if sum(y)==k:
        print(y)


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]
#  Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
# print(dict(zip(list1,list2)))
kl = dict(zip(list1,list2))
# print(sorted(kl.items(),key= lambda x:x[1]))
# drt = sorted(kl.items(),key= kl.values())
# print("KILO====",kl)
drt = sorted(kl.items(),key= lambda x:x[1])
# print("DRT---",drt)
# dr = sorted(kl,key= lambda x:x[1])
lo = []
lo1 = [y[0] for y in drt]
# print("LO111111===",lo1)
for y in drt:
    lo.append(y[0])

print("LO====",lo)

            