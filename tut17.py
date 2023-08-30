
# union and intersection in python 

A = {1, 2, 3}
B = {3, 4,1}
union = A.union(B)
print(union)

union_res = A|B
print(union_res)


intersect = A.intersection(B)
print(intersect)

inter = A&B
print(inter)

# Remember that both methods return new 
# sets and do not modify the original sets.
# If you need to modify the original sets, you
# can use the update() method for union and the 
# intersection_update() method for intersection.

# A.update(B)
# print(A)

A.intersection_update(B)
print(A)
