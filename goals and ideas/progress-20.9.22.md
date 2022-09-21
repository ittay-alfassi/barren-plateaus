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
-   Wrote experiment code for hald-MUBs (Tal's idea).

Code to Write:
-   Separate analysis functions for using k random starting parameters

Tested Issues and modifications:
-   Started running Jupyter Notebooks on Newton (the faculty HPC cluster) to get better computing power :)
-   Ditched using qiskit-aer-gpu. According to Dekel, it's only useful at around ~16 qubits.
-   Changed the initial parameter vector to sample from $[-\pi, \pi)$ and not $[0,1)$.

Issues & Modifications to tackle:
-   See how different correctness bounds affect the choice of k mub states / k random angles.
-   Write result analysis code for k half-MUBs.
-   When using COBYLA on a linux machine, a weird warning popped up. No idea what it was or what caused it.
    Try and see if you can reproduce it.
-   Add a modification for "save-as" for results, to save multiple results for arbitrary experiments.
-   Save graphs for all of the results you generated!



Kinds of experiment runs:
-   All MUB states for 3 qubits
-   k random MUB states (as initial states) for 3 qubits with the same initial vector
-   k different initial vectors, with the same initial state (|0>), for 3/n qubits
-   k states in which a pair is in a MUB state, and the rest are in 0.

Hyper-parameters to check:
-   Optimizer (COBYLA/Powell/SLSQP)
-   Correctness bound (0.4/e-1/e-2)
-   tol value (e-1/e-3/e-5/e-12)
-   solved problem (VQC/VQE/SSVQE)

Results to compare:
-   Convergence Graph
-   nfev
-   success to reach correctness bound (in percents)

Standard experiment details:
-   VQC barren plateaus (as shown in Arrasmith)
-   7 layers, 3 qubits
-   Low tol, low correctness bound
-   k = 25 (for good statistics)

Planned Experiments:
### Optimizer-based
-   On the standard experiment, test times for different optimizers (k MUB vs k random)
COBYLA gives 46s on standard with k MUBs (very random results...).
COBYLA gives 32s on standard with k random thetas.
SLSQP gives avg 34.4s on standard with k MUBs.
SLSQP gives avg 52.8s on k random thetas.

-   On the no-MUB experiment, test times for different optimizers (n=4...7)
COBYLA, as usual, works fine.
SLSQP worked terribly for some reason.
Nelder-Mead was also very bad.
Powell seems to work ok.
The "interesting" boundary is 7 layers.

-   On the standard experiment, test different correctness bounds x different optimizers (k MUB vs k random)
With 0.4 for a correctness bound, there is no difference. The "task" is very easy, but was a bit shorter with k random.

-   On the standard experiment, test different tol x different optimizers (k MUB vs k random)

If we have apparent differences, pick the faster optimizer.
If not, this case might be not interesting...

### Optimizer-based: n qubits
-   Fix a standard n. (from no-MUB)
-   On the standard experiment, test times for different optimizers (k half-MUB vs k random)
-   On the standard experiment, test different correctness bounds x different optimizers (k MUB vs k random)

At this point, either all optimizers act the same or there is one better choice.

### k-based
-   On a standard (maybe harder?) experiment, test different values of k x correctness x tol.
    For every such experiment, check the minimum nfev for k random angles and k random MUBs.
    
### k-basee: n qubits
-   Do the same with the n found earlier.

After these experiments, it should be clear whether there is any advantage to using MUBs with VQC.