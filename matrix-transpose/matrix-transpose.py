import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row = len(A);
    col = len(A[0])
    b = np.ndarray((col, row))

    for r in range(row):
        for c in range(col):
            b[c][r] = A[r][c]

    return b
