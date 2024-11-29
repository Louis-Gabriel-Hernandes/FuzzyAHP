import numpy as np

# Define triangular fuzzy number
def triangular_fuzzy_number(l, m, u):
    return (l, m, u)

# Generate fuzzy comparison matrix
def generate_fuzzy_matrix(n, scale):
    fuzzy_matrix = np.zeros((n, n, 3))  # Triangular fuzzy numbers
    for i in range(n):
        for j in range(n):
            if i == j:
                fuzzy_matrix[i, j] = (1, 1, 1)  # Diagonal elements
            else:
                fuzzy_matrix[i, j] = scale[i][j]
                fuzzy_matrix[j, i] = (1/scale[i][j][2], 
                                      1/scale[i][j][1], 1/scale[i][j][0])  # Reciprocal
    return fuzzy_matrix

# Fuzzy synthesis
def fuzzy_synthesis(fuzzy_matrix):
    row_sums = np.sum(fuzzy_matrix, axis=1)
    total_sum = np.sum(row_sums, axis=0)
    return row_sums / total_sum

# Defuzzify fuzzy weights
def defuzzify(fuzzy_weights, alpha=0.5):
    crisp_weights = [alpha * w[2] + (1 - alpha) * 
                     w[0] for w in fuzzy_weights]
    return crisp_weights

# Example
criteria = ["C1", "C2", "C3"]
scale = [
    [(1, 1, 1), (1/2, 1, 3/2), (1/3, 1/2, 1)],
    [(2/3, 1, 2), (1, 1, 1), (1/2, 1, 3/2)],
    [(1, 2, 3), (2/3, 1, 2), (1, 1, 1)]
]

fuzzy_matrix = generate_fuzzy_matrix(len(criteria), scale)
fuzzy_weights = fuzzy_synthesis(fuzzy_matrix)
crisp_weights = defuzzify(fuzzy_weights)

print("Crisp Weights:", crisp_weights)


def calculate_eigenvector(crisp_weights):
    """
    Normalize the crisp weights to calculate eigenvector for ranking.
    """
    total = sum(crisp_weights)
    return [cw / total for cw in crisp_weights]

def consistency_check(matrix, n):
    """
    Check if the consistency index (CI) is less than 0.1.
    """
    # Compute CR = CI / RI where RI = Random Index (depends on n)
    pass  # Placeholder for CI calculation

def sensitivity_analysis(crisp_weights):
    """
    Analyze the sensitivity of criteria based on variations in weights.
    """
    pass  # Placeholder for sensitivity analysis