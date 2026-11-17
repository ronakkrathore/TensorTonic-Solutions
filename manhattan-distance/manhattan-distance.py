import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    dis = 0.0

    for xi, yi in zip(x, y):
        dis += np.abs((xi-yi))

    return dis