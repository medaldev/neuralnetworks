from random import random
from pprint import pprint
from numpy import exp
from time import sleep

COUNT_LAYERS = 2
COUNT_INNER_LAYERS = 0
COUNT_INPUT_NEURONS = 2
COUNT_OUT_NEURONS = 1
COUNT_INNER_NEURONS = 0
neurons = []


def activation_function(x):
    return 3 * x

class Neron:
    def __init__(self, value=0, parents=list(), parent_weights=list(), children=list(), children_weights=list()):
        self.value = value
        self.parents = parents
        self.children = children
        self.parents_weights = parent_weights
        self.children_weights = children_weights

    def print_weights(self):
        pprint(self.parents_weights)

    def activate(self):
        self.value = sum(self.parents[i].value * self.parents_weights[i] for i in range(len(self.parents)))
        return activation_function(self.value)

    def __repr__(self):
        return str(self.value)


def activate():
    for layer in range(1, len(neurons)):
        for neuron in neurons[layer]:
            neuron.activate()
    print("Res:", neurons[1][0])
    return neurons[1][0].value

def generate_weights():
    global weights
    weights.append([random() for _ in range(len(neurons[-1]))])
    return weights[-1]

def get_weight_neron(obj, layer):
    for n in range(len(neurons[layer])):
        if obj in neurons[layer][n].parents:
            return neurons[layer][n].parents.index(obj)


def learning(output):
    y = activate()
    E = 0.5 * ((y - output) ** 2)
    print("Error:", E)
    neurons.reverse()
    for i in range(1, len(neurons)):
        # e = E * neurons[i - 1][0].parents_weights[get_weight_neron(neurons[i][j], i - 1)]

        for j in range(len(neurons[i])):
            w = get_weight_neron(neurons[i][j], i - 1)
            neurons[i - 1][0].parents_weights[w] += 0.04 * (E / neurons[i - 1][0].parents_weights[w])
    neurons.reverse()

weights = []

neurons.append([Neron() for _ in range(COUNT_INPUT_NEURONS)])
neurons.append([Neron(parents=neurons[-1],
                      parent_weights=generate_weights()) for _ in range(COUNT_OUT_NEURONS)])


def process(input_data, r):
    for n in range(len(neurons[0])):
        neurons[0][n].value = input_data[n]
    current = activate()
    while round(current, 2) != round(r, 2):
        print()
        learning(r)
        # sleep(0.02)
        print(neurons)
        print(weights)
        print()
        current = activate()

print("starting!")
print(weights)
input_data = [[-1, -1], [1, 1], [-2, -2], [10, 10], [-4, -4], [3, 3]]
for ex in input_data:
    process(ex, sum(ex))
    print(neurons)
    print(weights)

"""neurons[1][0].parents_weights = [0, 2][:]
neurons[0][0].value, neurons[0][1].value = 100, 100
activate()
neurons[0][0].value, neurons[0][1].value = 1, -3
activate()"""