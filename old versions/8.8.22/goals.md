Required data per BP problem:
1.  BP Scaling with 3 qubits, n layers: iters/layers
2.  BP Scaling with n qubits, n layers: iters/layers
3.  **Best** iters with MUB prepending, 3 qubits, n layers: iters/layers
4.  **Best** iters with MUB appending, 3 qubits, n layers: iters/layers
5.  **Amount** of advantageous MUB states prepending, 3 qubits, n layers: (average, #states)/MUB/layers
6.  **Amount** of advantageous MUBs appending, 3 qubits, n layers: (average, #MUBS)/layers


MUB generation:

-   Generate MUB circuits for 2 qubits (3,0,2)  [DONE]
-   Generate MUB circuits for 3 qubits (3,0,6)  [DONE]
-   Understand and formalize the method for n-qubit MUB matrices
-   Generate MUB circuits for n qubits

Variational Quantum Compilation Barren Plateaus:
-   Search for BPs with 3 qubits, n layers  [DONE]
    No "big" scaling problems.
-   Search for BPs with n qubits, n layers  [DONE]
    Big scaling problem detected!
-   Search for BP advantage with 3 qubits, n layers, by preparing MUB initial states [DONE]
-   Search for BP advantage with 3 qubits, n layers, by appending MUB transformations [DONE]
-   Get statistics for BP advantage with 3 qubits, n layers, prepending
-   Get statistics for BP advantage with 3 qubits, n layers, appending
-   Generate summarizing data


Variational Quantum Eigensolver (VQE) Barren Plateaus:
-   Search for BPs with 3 qubits, n layers  [DONE]
    No "big" scaling problems.
-   Search for BPs with n qubits, n layers
-   Search for BP advantage with 3 qubits, n layers, by preparing MUB initial states
-   Search for BP advantage with 3 qubits, n layers, by appending MUB transformations [DONE]
-   Get statistics for BP advantage with 3 qubits, n layers, prepending
-   Get statistics for BP advantage with 3 qubits, n layers, appending [DONE]