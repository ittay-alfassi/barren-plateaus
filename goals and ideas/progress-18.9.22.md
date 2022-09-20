Progress report: 18.9.22

Design Choices:
-   Reunited barren plateau notebooks, becuase of code duplication being a pain.
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
-   Started running Jupyter Notebooks on Newton (the faculty HPC cluster) to get better computing power :)
-   Ditched using qiskit-aer-gpu. According to Dekel, it's only useful at around ~16 qubits.
-   Changed the initial parameter vector to sample from $[-\pi, \pi)$ and not $[0,1)$.

Issues & Modifications to tackle:
-   See how different correctness bounds affect the choice of k mub states / k random angles.

-   When using COBYLA on a linux machine, a weird warning popped up. No idea what it was or what caused it.
    Try and see if you can reproduce it.
-   Trythe pair method described by Tal (for all pairs of qubits, try all MUB states and 0 in the rest).


Kinds of experiment runs:
-    All MUB states for 3 qubits
-    k random MUB states (as initial states) for 3 qubits with the same initial vector
-    k different initial vectors, with the same initial state (|0>), for 3/n qubits
-    k states in which a pair is in a MUB state, and the rest are in 0.

Hyper-parameters to check:
-    Optimizer (COBYLA/Powell/SPSA)
-    Correctness bound (0.4/e-1/e-2)
-    k (2/5/10/20)
-    tol value (e-1/e-3/e-5/e-12)
-    solved problem (VQC/VQE/SSVQE)

Results to compare:
-    Convergence Graph
-    nfev
-    success to reach correctness bound (in percents)