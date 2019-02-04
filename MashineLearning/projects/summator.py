from random import random, randint
from pprint import pprint
from numpy import exp
from time import sleep


structure = [2, 1]
nerons = [[0 for i in range(structure[layer])] for layer in range(len(structure))]
weights = {}

def activation_function(x):
    return 1 * x


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
                weights[(f"{i}{j}", f"{i - 1}{past}")] += 0.0000005 * (nerons[i][j] / weights[(f"{i}{j}", f"{i - 1}{past}")])

init_weights()
input_data = [[randint(-50, 50), randint(0, 50)] for _ in range(200)]
print(input_data)
for epoha in range(950):
    print("Эпоха", epoha, "*" * 64)
    for k, ex in enumerate(input_data):
        work = start(ex)
        print("Стадия обучения", k)
        print("Выход: ", work)
        print("Правильно", sum(ex))
        print(weights)
        print()
        learn(sum(ex))
        work = start(ex)
        # sleep(0.2)
print(weights)

"""
Стадия обучения 199
Выход:  35.75980067805526
Правильно 35
{('10', '00'): 0.991168712033552, ('10', '01'): 1.0420685099802636}

{('10', '00'): 0.9911688576437451, ('10', '01'): 1.0420686484781323}

Process finished with exit code 0


"""