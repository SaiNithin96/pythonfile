# Sets -- sequence of elements seperated with comma(,) which are declared inside { } which 
# doesnot contain duplicate.

a={2,3,4,5,6,7,2}

# print(a)

# Sets are Mutuable but element which are declaring should be of immutable datatypes only.

# b={2,'python',5.6,(4,5,6),[7,8,9]}

# print(b)

# sets are unordered datatypes we cannot predict the order how it takes..

# Adding or updating the elements inside the set.

# print(dir(set))


#add --- adding single element into the sets.. all the element declaring should be of immutable..

# a.add('program')

# print(a)

# a.add((4,5,6))
# print(a)

# update  -- for adding multiple element into the set at a time..(only iterables..)

a.update('python',[11,12,13],(21,22,23),{31,32,33})
print(a)


# removing the elements

# remove -- is for removing the particular element
# a.remove(42)
# print(a)

# discard -- same as remove but will not do anything if the element is not in the set.
# a.discard(42)
# print(a)

# print(a.pop())
# print(a)

# print(a.pop())
# print(a)

a.clear()
# print(a)


# a={}
# b={}

c=set()  # Empty set..

# Set Operations

	#1)Union(|)
	#2)Intersection(&)
	#3)Difference(-)
	#4)Symmetric Difference(^)

a={2,3,4,5,6,7}
b={6,7,8,9,0,1}

# Union -- Adding of both the sets and removing the duplicates..

# print(a|b)
# print(a.union(b))


# Intersection  -- Common elements in both the sets..

# print(a&b)
# print(a.intersection(b))

# Difference  -- Removing common elements and retunr only element from first variables..

# print(a-b)
# print(a.difference(b))

# print(b-a)
# print(b.difference(a))


# SymmetricDifference  -- 

# print(a^b)
# print(a.symmetric_difference(b))
# print(b^a) 


# print(dir(set))


a={2,3,4,5,6,7}
b={6,7,8,9,0,1}


# print(a.intersection(b))
# a.intersection_update(b)

# print(a)

# a.difference_update(b)

# print(a)

# a.symmetric_difference_update(b)
# print(a)


#isdisjoint  -- Not common elements between both the sets.

# a={2,3,4,5}
# b={6,7,8,9,2}

# print(a.isdisjoint(b))

# a={2,3,4,6,7,8}
# b={4,8}


# print(a.issubset(b))
# print(a.issuperset(b))

a={4,5,6,7}
# b=a
# copy -- taking values as the reference and creating a new location with the values...

# print(a)
# print(b)

# b.add(8)

# print(a)
# print(b)

b=a.copy()

print(id(a))
print(id(b))

b.add(8)

print(a)
print(b)