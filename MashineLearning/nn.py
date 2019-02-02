import json
import random


# <Constants>
PATH_SAVES = "saves/"
# </Constants>

# <Variables>

in_count = None
all_inners_count = None
inner_count = None
out_count = None

Neurons_in = []
Neurons_hidden = []
Neurons_out = []
Dependences_hidden = []
Dependences_out = []
# </Variables>

def importing(filename):
    global inner_count, all_inners_count, inner_count, out_count
    with open(PATH_SAVES + "/" + filename, "r", encoding="utf8") as base:
        base = json.loads(base.read())
        in_count, all_inners_count, = base["in_count"], base["all_inners_count"]
        inner_count, out_count = base["inner_count"], base["out_count"]
        weights = base["weights"]
    return in_count, all_inners_count, inner_count, out_count, weights

def init(in_count, all_inners_count, inner_count, out_count, weights=None):
    global Dependences, Neurons




def save():
    with open(f'{PATH_SAVES}/neuroset-{time()}.json', "w", encoding="utf8") as jsonfile:
        data = {"in_count": in_count,
                "all_inners_count": all_inners_count,
                "inner_count": inner_count,
                "out_count": out_count,
                "weights": Dependences}
        json.dump(data, jsonfile)


init(3, 4, 4, 1, [[[1, 2, 3], ]])
print(Neurons)
print(Dependences)