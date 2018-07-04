# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
import itertools

a=map(int,raw_input().split(' '))
b=map(int,raw_input().split(' '))
print (*list(itertools.product(a,b)))
