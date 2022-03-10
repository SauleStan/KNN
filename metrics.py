from cmath import sqrt

def euclidean_distance(vector1, vector2):
    # Store the number of dimensions
    dim = len(vector1)
    # Set initial distance to 0
    distance = 0
    # Calculate euclidean distance
    for d in range(dim):
        distance += sqrt((vector1[d]-vector2[d])**2)
    
    return distance

def manhattan_distance(vector1, vector2):
    # Store the number of dimensions
    dim = len(vector1)
    # Set initial distance to 0
    distance = 0
    # Calculate euclidean distance
    for d in range(dim):
        distance += abs(vector1[d]-vector2[d])
    return distance
