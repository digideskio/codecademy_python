# Write your function below!
def fizz_count(x):
    """Takes a list and returns the number of times the string 'fizz' occurs in the list"""
    count = 0
    for word in x:
        if word == "fizz":
            count += 1

    return count


