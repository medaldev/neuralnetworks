import numpy as np
import json
from random import randint
from random import random
from time import time


PATH_SAVES = "saves/"


def activation_function(x, derivative=True):
    return 1 / (1 + np.exp(-1 * x))


class AbstractNeuralNetwork:

    def run(self):
        for layer in self.network[1]:
            for neuron in layer:
                neuron.activation()
        for neuron in self.network[2]:
            neuron.activation()
        return self.network[2]

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


    def _init_layer_dependences(self):
        for layer in range(len(self.network[1])):
            for n in range(len(self.network[1][layer])):
                if n == 0:
                    self.network[1][layer][n].add_dependences(self.network[0])
                else:
                    self.network[1][layer][n].add_dependences(self.network[1][layer-1])
        for neuron in self.network[2]:
            neuron.add_dependences(self.network[1][-1])


class NeuralNetwork(AbstractNeuralNetwork):
    def __init__(self, in_count, all_inners_count, inner_count, out_count):
        self.in_count = in_count
        self.all_inners_count = all_inners_count
        self.inner_count = inner_count
        self.out_count = out_count
        self.network = [[Neuron() for n in range(in_count)],
                        [[Neuron() for n in range(inner_count)] for layer in range(all_inners_count)],
                        [Neuron() for n in range(out_count)]
                        ]

        self._init_layer_dependences()

class NeuralNetworkImport(AbstractNeuralNetwork):
    def __init__(self, filename):
        with open(PATH_SAVES + "/" + filename, "r", encoding="utf8") as base:
            base = json.loads(base.read())
            in_count, all_inners_count, = base["in_count"], base["all_inners_count"]
            inner_count, out_count = base["inner_count"], base["out_count"]
            weights = base["weights"]
        self.in_count = in_count
        self.all_inners_count = all_inners_count
        self.inner_count = inner_count
        self.out_count = out_count
        self.network = [[Neuron() for n in range(in_count)],
                        [[Neuron() for n in range(inner_count)] for layer in range(all_inners_count)],
                        [Neuron() for n in range(out_count)]
                        ]
        self._init_layer_dependences(weights)

    def _init_layer_dependences(self, weights=None):
        print("w", weights)
        for layer in range(len(self.network[1])):
            for n in range(len(self.network[1][layer])):
                if n == 0:
                    self.network[1][layer][n].add_dependences(self.network[0], weight=weights[0][0])
                else:
                    self.network[1][layer][n].add_dependences(self.network[1][layer-1], weight=weights[0][layer])
        for neuron in self.network[2]:
            neuron.add_dependences(self.network[1][-1], weight=weights[1])


class Neuron:
    def __init__(self, value=None):
        self.dependences = {}
        self.value = value if value else randint(0, 1)

    def add_dependences(self, neurons, weight=random()):
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


network = NeuralNetwork(3, 2, 4, 1)
print(network.get_all_weights())
# network.run()
# print(network.network)
# print(network.network[1][0][0].dependences)
network.save()
print("################")
imp = NeuralNetworkImport("neuroset-1539459749.0751953.json")
print(imp.get_all_weights())