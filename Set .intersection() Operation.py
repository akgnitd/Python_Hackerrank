n=int(input())
n1=input()
c=[int(i) for i in set(n1.split(' '))]
m=int(input())
m1=input()
d=[int(j) for j in set(m1.split(' '))]
k=set(c).intersection(set(d))
print(len(k))
