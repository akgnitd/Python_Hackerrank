n=int(input())
str_n=input()
list1={int(element) for element in set(str_n.split(' '))}
m=int(input())
str_m=input()
list2={int(element) for element in set(str_m.split(' '))}
unionset=list1.union(list2)
print(len(unionset))
