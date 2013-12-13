m = [1, 2, 3]
n = [4, 5, 6]
o = [7, 8, 9]

# Update the below function to take
# an arbitrary number of arguments
def join_lists(*args):
    res = []
    for lst in args:
        res += lst
    return res


print join_lists(m, n, o)
