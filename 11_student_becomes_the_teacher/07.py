lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(lst):
    sum = 0
    count = 0
    for score in lst:
        sum += score
        count += 1

    return float(sum) / float(count)

def get_average(student):
    homework = average(student["homework"]) * .1
    quizzes = average(student["quizzes"]) * .3
    tests = average(student["tests"]) * .6
    return homework + quizzes + tests
