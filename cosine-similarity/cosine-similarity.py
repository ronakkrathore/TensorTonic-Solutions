import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dot=0.0

    for i in range(len(a)):
        dot += a[i]*b[i]

    SqsumA=0.0;

    for ele in a:
        SqsumA += ele **2

    magA = np.sqrt(SqsumA) 

    sqSumB = 0.0
    for ele in b:
        sqSumB += ele**2

    magB = np.sqrt(sqSumB)

    if magA == 0 or magB == 0:
        return 0.0
        

    return float(dot/(magA * magB))