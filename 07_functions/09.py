def cube(n):
    return n**3

def by_three(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return False

print by_three(9)
print by_three(4)
