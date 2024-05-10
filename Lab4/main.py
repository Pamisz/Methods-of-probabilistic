import numpy as np
import random
n = 100000
numbers = [[0.1, 0, 0, 0.4],
           [0.2, 0, 0, 0],
           [0, 0.1, 0, 0.1],
           [0, 0, 0.1, 0]]

def generateX():
    rand_val = random.random()
    s1 = sum(numbers[0])
    s2 = sum(numbers[1])
    s3 = sum(numbers[2])
    if rand_val < s1:
        return 1
    elif rand_val < s1 + s2:
        return 2
    elif rand_val < s1 + s2 + s3:
        return 3
    else:
        return 4

def generateY(x):
    rand_val = random.random()
    c = sum(numbers[x-1])
    s1 = numbers[x-1][0] / c
    s2 = numbers[x-1][1] / c
    s3 = numbers[x-1][2] / c
    if rand_val < s1:
        return 1
    elif rand_val < s1 + s2:
        return 2
    elif rand_val < s1 + s2 + s3:
        return 3
    else:
        return 4

def generate():
    x = generateX()
    y = generateY(x)
    return x, y

points = [generate() for _ in range(n)]

counts = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in points:
    counts[i[0]-1][i[1]-1] += 1

print(counts)

