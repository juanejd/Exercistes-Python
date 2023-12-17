# Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    # new_lst = []
    # for i in lst:
    #     j = i * 2
    #     new_lst.append(i-j)
    # return new_lst
    return [(i - (i * 2)) for i in lst]

print(invert([1, -2, 3, -4, 5]))