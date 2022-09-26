from cmath import nan
import os
from ast import literal_eval
from pprint import pprint
import matplotlib.pyplot as plt


def foo(results_dict):
    layer = results_dict[list(results_dict.keys())[0]]
    layer['hit_hi_bound'] = {}
    evals = layer['evals']
    for index, eval_list in evals.items():
        if all([x > 0.4 for x in eval_list]):
            layer['hit_hi_bound'][index] = None
        else:
            layer['hit_hi_bound'][index] = eval_list.index(next(filter(lambda x: x <= 0.4, eval_list)))
    results_dict[list(results_dict.keys())[0]] = layer
    return results_dict

with open('VQC results\\7 qubit graphs\\random_7_qubit\\stats.txt', 'r+') as f:
    data = f.read()
    random_dict = literal_eval(data)
    random_dict_new = foo(random_dict)
    pprint(random_dict_new, f)

plt.plot([(x, 0) for x in random_dict_new[7]['hit_hi_bound'].values()], color='yellow')




with open('VQC results\\7 qubit graphs\\halfmub_7_qubit\\stats.txt', 'r+') as f:
    data = f.read()
    halfmub_dict = literal_eval(data)
    halfmub_dict_new = foo(halfmub_dict)
    pprint(halfmub_dict_new, f)

plt.plot([(x, 0) for x in halfmub_dict_new[7]['hit_hi_bound'].values()], color='blue')

plt.show()