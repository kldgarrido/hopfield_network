
import numpy as np


def discretize(number):
    if number<0.0:
        return -1.0
    else:
        return 1.0


def train(data):
    sum_matrix = []
    for matrix in data:
        a = np.array(matrix).transpose()
        b = np.array(matrix)
        temp = np.matmul(a, b)
        sum_matrix.append(temp)
    return sum_matrix


def clasifier(pattern, matrix_weight):
    temp = np.matmul(pattern, matrix_weight)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i,j]=discretize(temp[i,j])
    return temp


def sum_vector(vectors):
    result = vectors[0]
    for i in range(1,len(vectors)):
        result += vectors[i]
    return result


def execute(data_pattterns, clasifier_pattern):
    vectors_matrix_weight = train(data_pattterns)
    matrix_weight = sum_vector(vectors_matrix_weight)
    np.fill_diagonal(matrix_weight, 0)
    clasified_pattern = clasifier(clasifier_pattern, matrix_weight)
    return clasified_pattern
