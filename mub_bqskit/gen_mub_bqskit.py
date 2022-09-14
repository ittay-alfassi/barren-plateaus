#  Written by Ittay Alfassi.

from qiskit.opflow import X, Y, Z, I
from qsymm.linalg import simult_diag
import numpy as np
from bqskit.compiler import Compiler
from bqskit.compiler import CompilationTask

def mats_to_mub_circ(mats_row: np.ndarray, nqubits: int):
    mub_uni = np.hstack(simult_diag(mats_row))
    task = CompilationTask.synthesize(mub_uni)
    with Compiler() as compiler:
        synth_qc = compiler.compile(task)
    return mub_uni, synth_qc.to('qasm')


tbl_2_302 = [ [Z^I, I^Z, Z^Z],
        [X^I, I^Y, X^Y],
        [Y^I, I^X, Y^X],
        [Y^Y, Z^X, Z^X],
        [X^X, Y^Z, Z^Y]]

tbl_3_306 = [   # The full columns were not added, as to save space, since 3 matrices should define the basis completely.
    [X^I^I, I^Y^I, I^I^Z, X^Y^Z, X^Y^I, X^I^Z, I^Y^Z],  # First 3 rows are product state bases
    [Y^I^I, I^Z^I, I^I^X],
    [Z^I^I, I^X^I, I^I^Y],
    [Y^Z^Z, Z^Y^Z, Z^Z^Y],  # Last 6 rows are GHZ-like bases
    [Z^X^X, X^Z^X, X^X^Z],
    [X^Y^Y, Y^X^Y, Y^Y^X],
    [Z^X^Z, Y^X^X, Y^Y^Z],
    [X^Y^X, Z^Y^Y, Z^Z^X],
    [Y^Z^Y, X^Z^Z, X^X^Y]
]

print('----------RESULTS FOR 2-QUBIT MUBS (3,0,2)--------------')
for i, row in enumerate(tbl_2_302):
    res = mats_to_mub_circ(list(map(lambda p: p.to_matrix(), row)), 2)
    print(f'result for row {i+1}:')
    print(res[0])
    print(res[1])
    print('\n')


print('----------RESULTS FOR 3-QUBIT MUBS (3,0,6)--------------')
for i, row in enumerate(tbl_3_306[0:1]):
    res = mats_to_mub_circ(list(map(lambda p: p.to_matrix(), row)), 3)
    print(f'result for row {i+1}:')
    print(res[0])
    print(res[1])
# mats = list(map(lambda p: p.to_matrix(), tbl_2_302[0]))
# print(mats_to_mub_circ(mats, 2))
