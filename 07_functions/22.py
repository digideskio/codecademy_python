def distance_from_zero(n):
    if type(n) != int and type(n) != float:
        return "Not an integer or float!"
    else:
        return abs(n)

# Tests
print distance_from_zero("some string") # expect "not..."
print distance_from_zero("-20") # expect "not..."
print distance_from_zero(-100) # expect 100
print distance_from_zero(-20.0) # expect 20.0
print distance_from_zero(20.0) # expect 20.0

