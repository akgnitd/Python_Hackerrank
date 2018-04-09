m= int(input())
m1= input()
c=[int(i) for i in set(m1.split(" "))]
n= int(input())
n1= input()
d=[int(j) for j in set(n1.split(" "))]
e=set(c).union(set(d)) - set(c).intersection(set(d))
e=list(sorted(e))
for x in range(len(e)):
    print(e[x])
