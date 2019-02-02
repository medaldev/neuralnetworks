from random import random
from pprint import pprint

in_count = 9
all_inners_count = 2
inner_count = 4
out_count = 2

values = [[0 for _ in range(in_count)]] + [[0 for _ in range(inner_count)] for _ in range(all_inners_count)] + [[0 for _ in range(out_count)]]
weights = []
weights.append([[] for _ in range(in_count)])
weights.append([[random() for _ in range(in_count)] for _ in range(inner_count)])
for _ in range(all_inners_count - 1):
    weights.append([[random() for _ in range(inner_count)] for _ in range(inner_count)])
weights.append([[random() for _ in range(inner_count)] for _ in range(out_count)])

def start():
    for layer in range(1, len(values)):
        for value in range(len(values[layer])):
            values[layer][value] = activation(values[layer-1], weights[layer][value])
    return values[-1]

def activation(layer, dependences):
    result_sum = 0
    for v in range(len(layer)):
        result_sum += layer[v] * dependences[v]
    return activation_function(result_sum)

def activation_function(x):
    import numpy as np
    return 1 / (1 + np.exp(-1 * x))


def learning(examples, answers):
    for i in range(len(examples)):
        values[0] = [i for i in examples[i].copy()]
        res = start()
        if res != examples[i]:
            pass


start()
print(values)
