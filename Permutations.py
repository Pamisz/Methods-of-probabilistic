import math
towns = [
    [1, "Paris", 2138, 48.8566, 2.3522],
    [2, "Marseille", 861, 43.2965, 5.3699],
    [3, "Lyon", 515, 45.7578, 4.8320],
    [4, "Toulouse", 479, 43.6047, 1.4442],
    [5, "Nice", 342, 43.7102, 7.2620],
    [6, "Nantes", 309, 47.2184, -1.5536],
    [7, "Strasbourg", 280, 48.8566, 2.3522],
    [8, "Montpellier", 285, 43.6110, 3.8767],
    [9, "Bordeaux", 256, 44.8378, -0.5792],
    [10, "Lille", 232, 50.6292, 3.0572],
    [11, "Rennes", 216, 48.1173, -1.6778],
    [12, "Reims", 196, 49.2583, 4.0317],
    [13, "Le_Havre", 173, 49.4938, 0.1077],
    [14, "Saint-Etienne", 172, 45.4397, 4.3872],
    [15, "Toulon", 170, 43.1242, 5.9280]
]

def tree(n, k, permutation, permutations):
    if len(permutation) == int(k):
        permutations.append(permutation.copy())
        return 

    for i in range(1, int(n) + 1):
        if i not in permutation:
            permutation.append(i)
            tree(n, k, permutation, permutations)
            permutation.pop()

#main
n = input("Podaj n:")
k = input("Podaj k:")

while int(k) > int(n):
    k = input("Podaj k:")

permutation = []
permutations = []
tree(n, k , permutation, permutations)
print("\nPermutacje:")
for i in range(len(permutations)):
    print(i+1, permutations[i])


#Uzupelnienie 1
min_index = 0
min_value = 0
for i in range(len(permutations)):
    distance = 0
    for j in range(int(k)):
        if j > 0:
            x1 = towns[permutations[i][j-1]-1][3]
            x2 = towns[permutations[i][j]-1][3]
            y1 = towns[permutations[i][j-1]-1][4]
            y2 = towns[permutations[i][j]-1][4]
            distance = distance + math.dist((x1, y1), (x2, y2))
    start_x = towns[permutations[i][0]-1][3]
    start_y = towns[permutations[i][0]-1][4]
    distance = distance + math.dist((x2, y2), (start_x, start_y))
    if min_value == 0:
        min_value = distance
        min_index = i
    elif distance < min_value:
        min_value = distance 
        min_index = i

print("\nPrzebieg najkrotszej trasy:")
for i in range(len(permutations[min_index])):
    print(towns[permutations[min_index][i]-1][1])
print("Dlugosc najkrotszej trasy:", min_value, "\n")


#Uzupelnienie 2
fifty = 0
for i in range(int(n)):
    fifty = fifty + towns[i][2]
fifty = fifty //2
print("\n50% mieszkancow N miast to:", fifty)

diff = 0
min_diff = float('inf')  
nearest_subset = []
for i in range(len(permutations)):
    sum = 0
    for j in range (len(permutations[i])):
        sum = sum + towns[permutations[i][j]-1][2]
    diff = abs(fifty - sum)
    if diff == 0:
        print("50% liczby mieszkancow N miast ma podzbior:",permutations[i])
        for h in range(len(nearest_subset)):
            print(towns[permutations[i][h]-1][1])
        break
    elif diff < min_diff:
        min_diff = diff
        nearest_subset = permutations[i]

if diff != 0:
    print("Najbliższa wartość do 50% liczby mieszkańców N miast ma podzbiór:", nearest_subset)
    for i in range(len(nearest_subset)):
        print(towns[nearest_subset[i]-1][1])
    print("Roznica wynosi:", min_diff)
#jest dla n =13, k = 4