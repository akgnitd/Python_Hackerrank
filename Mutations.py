a=input()
b=input()

c=b.split(' ')
del c[0]
c=''.join(c)
b=list(b)
b.pop()
b.pop()
b=''.join(b)
b=int(b)
a=list(a)
a[b]=c
a=''.join(a)
print(a)
