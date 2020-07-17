# Python file Created By Bibhuti

# a={1,9,3,"PYTHON"};
#
# print(a);
# print(type(a));
# print(a[0])  # not support indexing

a_dupp={3,1,2,9,7};
print(a_dupp);

# a_dupp={2,2,True,1};
# print(a_dupp);

# for i in a_dupp:
#     print(i);

# print(a_dupp.add(132))   # use to add single element , Tuples
# print(a_dupp)
# for i in a_dupp:
#     print(i);

# print(a_dupp.update([1,2,4])); # use to add multiple element
# print(a_dupp);

# print(a_dupp.update((1,2,3)));
# print(a_dupp);

# print(a_dupp.update({1,2,3}));
# print(a_dupp);

# print(a_dupp.remove(2));
# print(a_dupp);

# print(a_dupp.remove(8));  # If element is not present it will show erro
# print(a_dupp)

# print(a_dupp.discard(2))
# print(a_dupp);

# print(a_dupp.discard(8))  # If element is not present it will not show error
# print(a_dupp);

# a={1,2,3,4};
# b={3,4,5,6};
# print(a.difference(b));
# print(b.difference(a));

# a={1,2,3,4};
# b={3,4,5,6};
# c = (b.difference_update(a));   # Difference of a-b will update in a
# print(b);

# print(a_dupp.pop());      # use to delete last element but in set values are in unorder
# print(a_dupp);

# a={1,2,3,4};
# b={3,4,5,6};
# print(a.intersection(b));     # use for checkking common element
# print(a);

# a={1,2,3,4};
# b={3,4,5,6};
# print(a.intersection_update(b));
# print(a);

# a={3,4};
# b={3,4,5,6};
# print(a.issubset(b));
# print({1,2,3}.issubset(b));

# a={3,4};
# b={3,4,5,6};
# print(b.issuperset(a));

# a={3,4,7};
# b={3,4,5,6};
# print(b.issuperset(a));

# a=set((1,2,3));
# print(a);
# print(type(a));


# print({1,2,3}.__eq__({1,2,3}));
# print({1,2,3}.__eq__({1,3,2,2}));
# print({1,2,3}.__eq__({1,3,2}));


# a={3,4,7};
# b={3,4,5,6};
# print(b.union(a));