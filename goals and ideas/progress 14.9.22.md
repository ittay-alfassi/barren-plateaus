Progress report: 14.9.22

Design Choices:
-   Split the Barren Plateau reconstruction from Arrasmith to a different notebook.
-   Added support for Nelder-Mead in the optimizers.
-   Got rid of the appended MUB sections.
-   Changed the prepend-mub data structure:
    Instead of a dictionary of layers, which contains a dictionary of mubs, which contains a dictionary of state results,
    I moved to a dictionary of layers, which contains a dictionary of (mub, comp_state) -> result.
    This is better suited for choosing k random states.

New Code Written:
-   Added convergence graphs and log-scaling of nfev(n_qubits) to all experiments.
-   Added support for saving data when using keyboard interrupts.
-   Added the Arrasmith ansatz, not only the Cerezo one.

Code to Write:
-   Separate analysis functions for using k random starting parameters

Tested Issues and modifications:
-   When using COBYLA with a 0 TOL, at some random iteration, all parameters would move to inf or -inf, making qiskit crash.
    When using any >0 TOL (even e-15), this issue does not happen, and optimization ends after a reasonable time.
    I presume that this happened when the optimizer has no idea what to do and "commits suicide".
    In any case, I am now testing with >0 TOL and seeing how things react.
-   Tried to use both COBYLA and Nelder-Mead. NM is highly sensitive to TOL values.
    An experiment with Cerezo(4,4), 0.1 success bound and a TOL of 0.02 caused an x15 slowdown compared to COBYLA.
-   I considered using the aer_statevector_simulator instead of the qasm_simulator out of curiosity.
    It only took longer, so I ditched it in favor of qasm.
-   I tried the Arrasmith ansatz, and not only the "easier" Cerezo one.
    The Barren Plateau problems are more apparent when using it - which is to be expected, as there are a LOT more parameters.

Issues & Modifications to tackle:
-   Try and open Jupyter Notebooks on Newton (the faculty HPC cluster) to get better computing power :)
-   Try and use qiskit-aer-gpu for faster circuit evaluations. (Linux only, install-from-source only, and a true pain in the ass.)
-   See how different correctness bounds affect the choice of k mub states / k random angles.
-   Change the initial parameter vector to sample from [-pi, pi) and not [0,1).
-   When using COBYLA on a linux machine, a weird warning popped up. No idea what it was or what caused it.
    Try and see if you can reproduce it.
-   Trythe pair method described by Tal (for all pairs of qubits, try all MUB states and 0 in the rest).
