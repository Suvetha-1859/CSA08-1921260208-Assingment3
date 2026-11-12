import copy
import sys
import time

rows, cols = 3, 4

# Aliasing problem
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Aliasing and copying
a = [[1, 2], [3, 4]]
alias = a
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 100

print("Original:", a)
print("Alias:", alias)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# Tuple unpacking
for lat, lon in stops:
    print("Latitude:", lat, "Longitude:", lon)

# Memory comparison
lst = list(range(1000))
tup = tuple(range(1000))

print("List Memory:", sys.getsizeof(lst))
print("Tuple Memory:", sys.getsizeof(tup))

# List inside tuple
data = ([10, 20], 30)
data[0].append(40)

print("Tuple with List:", data)
