A unitary 2-design for $D$ dimensions is a finite set $\{U_k\}_{k=1}^K \subset U(D)$ of unitary operators on $\mathbb{C}^D$ such that, for every polynomial $P(U)$ of degree at most 2 in the matrix elements of U and at most 2 in the complex conjugates of those matrix elements,

$$ \frac{1}{K} \sum_{k=1}^K P(U_k) = \int_{U(D)} dU P(U)$$

Where $U(D)$ is the unitary group over $D$ dimensions, and integrals over $U(D)$ are with respect to the unitarily invariant Haar measure.

If I understand the implications of the 2-design definition, they are:

1. Deep, random, unstructured circuits which form 2-designs on $n$ qubits will exhibit barren plateaus. (McClean)
2. Layered hardware efficient ansatzes with global cost functions will exhibit barren plateaus, even if shallow. (Cerezo)
3. Layered hardware efficient ansatzes form approximate 2-designs. (Harrow and Low)
4. NIBPs are a thing. (Wang)


