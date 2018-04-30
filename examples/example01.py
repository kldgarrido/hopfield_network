# Hopfield Network
from hopfield_core import execute


def run():
    data_pattterns = [
        [[1, 1, 1, -1]],
        [[-1, -1, -1, 1]],
    ]

    clasifier_pattern = [[-1, -1, -1, -1]]

    print("Pattern to clasifier:\n %s" % (clasifier_pattern))
    print('\n')

    clasified_pattern = execute(data_pattterns, clasifier_pattern)
    print("Clasified Pattern:\n %s" % (clasified_pattern))


run()