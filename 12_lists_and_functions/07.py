m = 5
n = 13
# Add add_function here!
def add_function(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print add_function(m, n)
