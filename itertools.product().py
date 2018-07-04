# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import product

a=map(int,raw_input().split(' '))
b=map(int,raw_input().split(' '))
print(*product(a,b))
