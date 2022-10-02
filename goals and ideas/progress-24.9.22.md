Progress report: 24.9.22

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

-   On the no-MUB experiment, test times for different optimizers (n=4...8)
COBYLA, as usual, works fine.
SLSQP worked terribly for some reason.
Nelder-Mead was also very bad.
Powell seems to work ok.
The "interesting" boundary is 7 layers.

With 8 qubits, I did two experiments.
In the first one, the Powell method managed to go "lower".
However, the two methods used a different initial vector (which, as we know, can affect the convergence greatly).

In the second, both used an identical initial vector, and both perform poorly.
My conclusion is that one is not really better than the other. If anything, COBYLA usually gives the better results.


-   On the standard experiment, test different correctness bounds x different optimizers (k MUB vs k random)
With 0.4 for a correctness bound, there is no difference between optimizers. The "task" is very easy, but was a bit shorter with k random.

With a correctness bound of 0.1 and COBYLA, MUB states had a small advantage over k random, but had around the same distribution.

With a correctness bound of 0.1 and Powell, only random thetas were tested, but took a LOT longer. a range of (559,1778) vs. (161,980)

-   On the standard experiment, test different tol x different optimizers (k MUB vs k random)
No big diff.

### Optimizer-based: n qubits
-   Fix a standard n. (from no-MUB)
took n=7 as the "interesting" limit, but it can take a lot time, so I tried 5 qubits in the meantime.

for n=5 and correctness of 0.1, random thetas went way better than MUBs.
About half of the MUBs even failed to converge.
This does have an explanation though: the states that have a "good" correctness probably lie outside the subspace that is spanned by the MUB+Ansatz.

An appropriate experiment with a high correctness definition is interesting.
-   On the standard experiment, test times for different optimizers (k half-MUB vs k random)
-   On the standard experiment, test different correctness bounds x different optimizers (k MUB vs k random)

At this point, either all optimizers act the same or there is one better choice.


Conclusions on optimizers:
the COBYLA optimizer is usually faster for the 3 qubit case with low correctness bounds.
with a larger number of qubits, though, Powell managed to go "lower" with the optimization.

### finding an advantage
-   On a standard (maybe harder?) experiment, test different values of k x correctness x tol.
    For every such experiment, check the minimum nfev for k random angles and k random MUBs.
    
### finding an advantage: n qubits
-   Do the same with the n found earlier.

After these experiments, it should be clear whether there is any advantage to using MUBs with VQC.


I did one main experiment.
The experiment compared VQC runs with random starting thetas vs different MUB pairs.
I used the Arrasmith ansatz with 7 qubits and layers.
I got 20 samples of random vectors and 22 samples of half-mub runs.
I used COBYLA with epsilonic (1e-123) tolerance, and a success bound of 0.1.

None of the experiments reached 0.1.
When checking at what iteration each experiment reached 0.4, both came up with rather similar distributions.
Same for final values.
My current conclusion is that there is no advantage to using Half-MUBs over random initial vectors.

However, there are other experiments to perform to confirm this conclusion.
