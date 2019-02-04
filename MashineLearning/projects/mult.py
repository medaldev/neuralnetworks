from random import random, randint
from pprint import pprint
from numpy import exp
from time import sleep


structure = [2, 3, 3, 1]
nerons = [[0 for i in range(structure[layer])] for layer in range(len(structure))]
weights = {}


def mult(arr):
    return arr[0] * arr[1]

def activation_function(x):
    return x


def init_weights():
    for i in range(1, len(nerons)):
        for j in range(len(nerons[i])):
            for past in range(len(nerons[i - 1])):
                weights[(f"{i}{j}", f"{i - 1}{past}")] = round(random(), 3)


def start(In):
    for k in range(len(In)):
        nerons[0][k] = In[k]
    for i in range(1, len(nerons)):
        for j in range(len(nerons[i])):
            res_sum = 0
            for past in range(len(nerons[i - 1])):
                res_sum += nerons[i - 1][past] * weights[(f"{i}{j}", f"{i - 1}{past}")]
            nerons[i][j] = activation_function(res_sum)
    return nerons[len(nerons) -1][0]

def learn(valid):
    for i in range(len(nerons) - 1, 0, -1):
        for j in range(len(nerons[i])):
            if (i, j) == (len(nerons) - 1, 0):
                nerons[i][j] = 0.5 * (nerons[i][j] - valid) ** 2
                # print(nerons[i][j])
            else:
                res_sum = 0
                for past in range(len(nerons[i + 1])):
                    res_sum += nerons[i + 1][past] * weights[(f"{i + 1}{past}", f"{i}{j}")]
                nerons[i][j] = activation_function(res_sum)
                nerons[i][j] = 0.5 * (nerons[i][j] - valid) ** 2
            for past in range(len(nerons[i - 1])):
                weights[(f"{i}{j}", f"{i - 1}{past}")] += 0.0000000005 * (nerons[i][j] / weights[(f"{i}{j}", f"{i - 1}{past}")])

init_weights()
input_data = [[randint(1, 5), randint(1, 5)] for _ in range(50)]
# input_data = [[-13, 49], [-40, 15], [-6, 30], [22, 34], [28, 49], [20, 21], [8, 32], [-43, 40], [-25, 47], [4, 38], [32, 22], [28, 13], [-3, 34], [-45, 31], [-50, 19], [-8, 1], [-1, 27], [-47, 19], [-5, 22], [14, 24], [-50, 41], [11, 4], [-30, 39], [-20, 16], [-40, 5], [30, 2], [-13, 39], [-21, 5], [-27, 4], [-2, 26], [41, 13], [3, 35], [4, 41], [-45, 46], [-27, 15], [42, 38], [29, 0], [-7, 30], [-41, 22], [-10, 26], [6, 1], [-31, 2], [35, 5], [-18, 6], [41, 47], [-36, 33], [33, 46], [-7, 12], [11, 11], [-19, 30], [-35, 16], [-16, 29], [24, 32], [4, 42], [0, 2], [8, 41], [-4, 33], [25, 32], [14, 24], [43, 5], [22, 28], [-44, 17], [-37, 0], [-13, 34], [25, 47], [-26, 18], [-20, 3], [-41, 43], [-15, 48], [-47, 40], [50, 50], [-26, 11], [49, 24], [18, 33], [-9, 32], [25, 19], [39, 12], [37, 36], [-9, 26], [23, 42], [23, 48], [11, 22], [28, 36], [-15, 0], [-16, 6], [34, 11], [-46, 35], [5, 34], [38, 9], [42, 30], [-25, 38], [-50, 16], [43, 23], [23, 16], [-19, 19], [-27, 11], [4, 5], [46, 20], [-12, 26], [48, 20], [34, 23], [-24, 50], [-44, 1], [-22, 26], [21, 2], [-25, 18], [0, 41], [33, 24], [15, 12], [22, 31], [-50, 35], [-23, 49], [32, 11], [-3, 38], [-21, 31], [-10, 29], [46, 42], [32, 8], [-40, 42], [-8, 39], [20, 34], [25, 46], [20, 14], [33, 14], [45, 12], [9, 22], [1, 0], [3, 38], [1, 3], [-45, 18], [-42, 13], [-2, 7], [9, 14], [-20, 18], [-12, 43], [2, 17], [-25, 16], [-45, 21], [0, 9], [-7, 32], [-25, 3], [22, 3], [-26, 33], [11, 7], [3, 41], [31, 41], [-40, 6], [-46, 2], [-29, 31], [43, 18], [-22, 48], [-40, 46], [18, 41], [-20, 45], [-42, 20], [38, 28], [2, 44], [-30, 45], [-3, 47], [-20, 19], [13, 33], [28, 35], [-12, 26], [-7, 15], [-48, 41], [-27, 27], [23, 35], [50, 0], [-4, 27], [-12, 38], [0, 37], [-42, 21], [-42, 34], [17, 37], [42, 18], [-20, 39], [49, 4], [-40, 2], [-14, 40], [-20, 32], [-20, 35], [43, 11], [-2, 8], [-16, 21], [43, 24], [22, 27], [47, 13], [49, 41], [-19, 11], [-16, 23], [25, 2], [-39, 36], [0, 50], [24, 13], [-16, 33], [-23, 38], [-46, 3], [50, 30], [-46, 20], [21, 42]]

print(input_data)
for epoha in range(1050):
    print("Эпоха", epoha, "*" * 64)
    for k, ex in enumerate(input_data):
        work = start(ex)
        print("Стадия обучения", k)
        print("Выход: ", work)
        print("Правильно", mult(ex))
        print(weights)
        print()
        learn(mult(ex))
        work = start(ex)
        # sleep(0.2)
print(weights)