import numpy as np
import json
from random import randint
from random import random
from time import time


PATH_SAVES = "saves/"

def activation_function(x, derivative=True):
    return 1 / (1 + np.exp(-1 * x))


class Neuron:
    def __init__(self, value=None):
        self.dependences = {}
        self.value = value if value else randint(0, 1)

    def add_dependences(self, neurons, weight):
        for neuron in neurons:
            self.dependences[weight] = self.dependences.get(weight, []) + [neuron]

    def activation(self):
        self.value = np.round(activation_function(self.__summator()))

    def __summator(self):
        res = 0
        for w, neurons in self.dependences.items():
            for n in neurons:
                res += n.value * w
        return res

    def __repr__(self):
        return str(self.value)


class NeuralNetwork:

    def __init__(self, in_count, all_inners_count, inner_count, out_count):
        self.in_count = in_count
        self.all_inners_count = all_inners_count
        self.inner_count = inner_count
        self.out_count = out_count

        self.neurons_in = [Neuron() for n in range(in_count)]
        self.neurons_hidden = [[Neuron() for n in range(inner_count)] for layer in range(all_inners_count)]
        self.neurons_out = [Neuron() for n in range(out_count)]
        self.set_weights()

    def set_weights(self, weights_in, weights_hidden, weights_out):
        if not weights_in: weights_in = [random() for _ in range(self.in_count)]
        if not weights_hidden:
            weights_hidden = [[random() for _ in range(self.inner_count)] for z in range(self.all_inners_count)]
        if not weights_out: weights_out = [random() for _ in range(self.out_count)]
        for neuron in self.neurons_in:
            neuron.add_dependences()

    def run(self):
        pass

    def save(self):
        with open(f'{PATH_SAVES}/neuroset-{time()}.json', "w", encoding="utf8") as jsonfile:
            data = {"in_count": self.in_count,
                    "all_inners_count": self.all_inners_count,
                    "inner_count": self.inner_count,
                    "out_count": self.out_count,
                    "weights": self.get_all_weights()}
            json.dump(data, jsonfile)

    def __get_all_neurons(self):
        result = []
        for layer in self.network[1]:
            for neuron in layer:
                result += [neuron]
        for neuron in self.network[2]:
            result += [neuron]
        return result

    def get_all_weights(self):
        weights = [[[list(n.dependences.keys()) for n in layer] for layer in self.network[1]],
                   [list(n.dependences.keys()) for n in self.network[2]]]
        return weights