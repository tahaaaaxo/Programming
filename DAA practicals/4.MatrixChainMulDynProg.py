def matrix_chain_order(p):
    # Compute the length of the input sequence p, which represents the dimensions
    # of a chain of matrices.
    n = len(p) - 1

    # Initialize two n x n tables to store the minimum cost of multiplying a
    # subchain of matrices and the optimal split positions.
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    # Iterate over subchain lengths from 2 to n, where n is the length of the chain.
    for l in range(2, n+1):
        # Iterate over all possible subchains of length l.
        for i in range(n-l+1):
            j = i + l - 1

            # Initialize the minimum cost to infinity.
            m[i][j] = float('inf')

            # Iterate over all possible split positions of the subchain and compute
            # the cost of multiplying the two resulting subchains and combining them.
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]

                # If the cost of this split is lower than the current minimum, update
                # the minimum cost and optimal split position.
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    # Return the minimum cost of multiplying the entire chain of matrices and the
    # optimal split positions.
    return m, s


def print_optimal_parens(s, i, j):
    # If the current subchain contains only one matrix, print its label.
    if i == j:
        print("A" + str(i), end="")
    else:
        # Otherwise, recursively print the optimal parenthesization of the two
        # subchains resulting from the optimal split position.
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")


# Example usage.
p = [30, 35, 15, 5, 10, 20, 25]
m, s = matrix_chain_order(p)
print_optimal_parens(s, 0, len(p)-2)
