import random


def generator(a, b):
    U = random.random()
    X = a + U * (b - a)
    return X


n = 100000
G = []
for _ in range(n):
    G.append(generator(50, 150))

test1 = 0
test2 = 0
test3 = 0
test4 = 0
test5 = 0
test6 = 0
test7 = 0
test8 = 0
test9 = 0
test10 = 0
zakres_start = 10
for i in range(n):
    if 0 < G[i] <= zakres_start + 50:
        test1 = test1 + 1

    if zakres_start + 50 < G[i] <= 2 * zakres_start + 50:
        test2 = test2 + 1

    if 2 * zakres_start + 50 < G[i] <= 3 * zakres_start + 50:
        test3 = test3 + 1

    if 3 * zakres_start + 50 < G[i] <= 4 * zakres_start + 50:
        test4 = test4 + 1

    if 4 * zakres_start + 50 < G[i] <= 5 * zakres_start + 50:
        test5 = test5 + 1

    if 5 * zakres_start + 50 < G[i] <= 6 * zakres_start + 50:
        test6 = test6 + 1

    if 6 * zakres_start + 50 < G[i] <= 7 * zakres_start + 50:
        test7 = test7 + 1

    if 7 * zakres_start + 50 < G[i] <= 8 * zakres_start + 50:
        test8 = test8 + 1

    if 8 * zakres_start + 50 < G[i] <= 9 * zakres_start + 50:
        test9 = test9 + 1

    if 9 * zakres_start + 50 < G[i] <= 10 * zakres_start + 50:
        test10 = test10 + 1
testy = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10]
print("Zadanie1: ", testy)

def generator2():
    rand_val = random.random()
    if rand_val < 0.1:
        return 1
    elif rand_val < 0.3:
        return 2
    elif rand_val < 0.6:
        return 3
    else:
        return 4


GEN = []
for _ in range(n):
    GEN.append(generator2())

test1 = 0
test2 = 0
test3 = 0
test4 = 0
for i in range(len(GEN)):
    if GEN[i] == 1:
        test1 = test1 + 1
    elif GEN[i] == 2:
        test2 = test2 + 1
    elif GEN[i] == 3:
        test3 = test3 + 1
    else:
        test4 = test4 + 1

testy = [test1, test2, test3, test4]
print("Zadanie2: ", testy)

