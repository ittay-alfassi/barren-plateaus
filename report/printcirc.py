import qiskit as qk
from qiskit import Aer, QuantumCircuit

from qiskit.circuit import Parameter, ClassicalRegister
from qiskit.circuit.library import EfficientSU2
from qiskit.utils import QuantumInstance
from qiskit.algorithms import VQE
from qiskit.algorithms.minimum_eigen_solvers.vqe import VQEResult
from qiskit.algorithms.optimizers import COBYLA
from typing import Tuple, List, Dict, Union
from scipy.optimize import minimize, OptimizeResult
import numpy as np
from random import random
import json
from pprint import pprint
import matplotlib.pyplot as plt
from operator import truediv
from cmath import pi
from random import randint
import os
import time

MUB_CIRC_2_PATH = os.path.join(os.getcwd(), 'mub_bqskit', '2_302')
MUB_CIRC_3_PATH = os.path.join(os.getcwd(), 'mub_bqskit', '3_306')

N_QUBIT_NO_MUB_PATH = 'no_mub_results_n.txt'
NO_MUB_PATH = 'no_mub_results_3.txt'
PRE_MUB_PATH = 'prepend_mub_results_3.txt'
K_PRE_MUB_PATH = 'prepend_k_mub_results_3.txt'
RANDOM_THETAS_PATH_3 = 'random_thetas_results_3.txt'

NO_MUB_GRAPH_FOLDER = '3 qubit graphs'
N_QUBIT_NO_MUB_GRAPH_FOLDER = 'n qubit graphs'

VQC_FOLDER = 'VQC results'

EPS_TOL = 1e-12
LO_TOL = 1e-5
MID_TOL = 1e-2
HI_TOL = 0.2
TINY_SUCCESS_BOUND = 0.01
LO_SUCCESS_BOUND = 0.1
HI_SUCCESS_BOUND = 0.4
N_QUBITS = 3

SHOTS = 8192
MAX_ITER = 1e8
qasm_backend = Aer.get_backend('qasm_simulator')
qasm_qi = QuantumInstance(qasm_backend, shots=SHOTS)

def gen_vqc_ansatz_cerezo(n_qubits: int, n_layers: int) -> QuantumCircuit:
    qc = qk.QuantumCircuit(n_qubits)

    idx = 0

    for i in range(n_qubits):
        theta = Parameter(f'θ_{idx}')
        idx += 1
        qc.ry(theta, i)
        

    for layer in range(n_layers):
        for i in range(0, n_qubits-1, 2):
            qc.cz(i, i+1)
        
        for i in range(n_qubits-1):
            theta1 = Parameter(f'θ_{idx}')
            idx += 1
            qc.ry(theta1, i)

        for i in range(1, n_qubits-1, 2):
                qc.cz(i, i+1)
            
        for i in range(1, N_QUBITS):
            theta2 = Parameter(f'θ_{idx}')
            idx += 1
            qc.ry(theta2, i)

    qc.measure_all()

    return qc


def gen_vqc_ansatz_arrasmith(n_qubits: int, n_layers: int) -> QuantumCircuit:
    qc = qk.QuantumCircuit(n_qubits)
    count=1
    for _ in range(n_layers):
        
        # First layer of U3 gates
        for i in range(n_qubits):
            thetas = [Parameter(f'θ_{count+z}') for z in range(3)]
            qc.u(*thetas, i)
            count += 3
            
        # First layer of even CXs
        for i in range(0, n_qubits-1, 2):
            qc.cx(i, i+1)
            
        # Second layer of U3 gates
        for i in range(n_qubits):
            thetas = [Parameter(f'θ_{count+z}') for z in range(3)]
            qc.u(*thetas, i)
            count += 3
            
        for i in range(1, n_qubits, 2):
            qc.cx(i, (i+1)%n_qubits)
            
    qc.measure_all()
        
    return qc


print(gen_vqc_ansatz_arrasmith(6,1))