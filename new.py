# l = [1,2,3,4]
from logging import raiseExceptions
from turtle import ScrolledCanvas


n = 16
s = 'ankit bose '
l = []
h = []
i = 1.0
count=0
for i in range(1,n+1):
    if i*i ==n:
        count+=1
        print(i*s)
else:
    i =1
    while i<=n+1:
        # print(i)
        if i*i ==n:
            print(s*int(i))
            count+=1
            break
        else:
            if round(n/(i*i),1)==1.0:
                count+=1
                print("val",i,int(i)*s)
        i+=0.1
        if count==1:
            break
# print(n, l, h)
# __init__.py
# folder py file
# setup.py
# license
# src wheel file .whl file
# test
l = [1,2,3,4,2,3,4]
# op = [1,2,3,4,-1,-1,-1] o(n)

j = []
op = []
for t in l:
    if t not in op:
        op.append(t)
    else:
        op.append(-1)
# []
r = []
# rate = lambda a: r.append(a) if a not in r else r.append(-1)
y = tuple(map(lambda n: r.append(n), filter(lambda n: n not in r,l)))
# print(rate, r)
print("yyyy",y)
#[]
r = []
d = list(map(lambda a:(r.append(a),r.append(0))[a not in r], l))
# d = list(map(lambda a:(-1,a)[a not in r], l))
print("-****",r,d)
dg = list(filter(lambda x: x in l, l))
print("dg========", dg)
# f = list(map(lambda x:d(x), l))
# print("f",f)
# for a in l:
#     print(d(a))
# print(r,set(r))
r = []
print(list(map(lambda a: (-1,a)[l.count(a)>1], l)))
print(r)
l = [1,2,3,4,2,3,4]
filtered_result = filter(lambda x: (l.count(x))==1, l) 
filtered_result12 = filter(lambda x: (l.count(x))>1, l) 
ht =[]
filtered_result45 = lambda x: (x not in ht)
filtered_result56 =lambda x: (x in ht)
# ht = []
rt = list(map(lambda n :ht.append(n) if filtered_result45(n) else ht.append(-1),l))
print("rtttt---------",rt, ht)
d = map(lambda a:(-1,a)[a not in r],l)
# print("==========dmap",list(d),r)
# filtered_result123 = list(map(lambda x:(0,-1) [l.count(x)>1], l))
# filtered_result1234 = list(map(lambda x:(x,l[x]) [x==0], filtered_result123))
print(list(filtered_result))
print(list(filtered_result12))
adder = lambda a: (r.append(-1),r.append(a)) [a not in r]

print("adder=======",adder,r)
r1 = list(filter(lambda d:d not  in adder(d), l))
print("adder12=======",adder,r1,r)
# print(filtered_result123)
# print(filtered_result1234)
# print(list(map((lambda x: x*2), range(3))))
# some_list =
# print((lambda some_list: list(map(lambda a: (r.append(-1),r.append(a))[a not in some_list],some_list)))([1,2,3,4,5,1,2,3]))