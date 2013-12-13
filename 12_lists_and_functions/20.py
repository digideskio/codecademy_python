n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(n):
    res = []
    for lst in n:
        res += lst
    return res



print flatten(n)
