n = int(input())
m = str(input())
l= [int(i) for i in set(m.split(" "))]
print(sum(l)/len(l))
