
import sys
from my_module import *
from my_module import find_index as fi, test
import antigravity

sys.path.append(sys.path[0]+'/modules')

from sub import sub

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math')
index2 = find_index(courses, 'Physics')

print(index)
print(index2)
print(test)
print(sys.path)  # folders which python will look for modules in order
print(sub(2, 3))
