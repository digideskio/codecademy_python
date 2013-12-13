n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(x):
    res = ""
    for s in x:
        res += s
    return res
    # or this:
    # return "".join(x)


print join_strings(n)
