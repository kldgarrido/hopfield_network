# Hopfield Network
from hopfield_core import execute
from utils import convert_vector_to_graph


if __name__ == '__main__':
    data_pattterns = [
        [[-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]],
        [[-1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]],
        [[1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1]],
    ]

    clasifier_pattern = [[-1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1]]

    output = convert_vector_to_graph(clasifier_pattern)
    print("Pattern to clasifier:\n %s" % (output))
    print('\n')

    clasified_pattern = execute(data_pattterns, clasifier_pattern)
    output = convert_vector_to_graph(clasified_pattern)
    print("Clasified Pattern:\n %s" % (output))
