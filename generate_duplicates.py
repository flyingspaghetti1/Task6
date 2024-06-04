import random


def generate_matrix(rows, columns):
    matrix = [[random.randint(0, 1) for _ in range(columns)] for _ in range(rows)]
    return matrix


def matrix_to_string(matrix):
    return ''.join(str(cell) for row in matrix for cell in row)


def write_to_file(filename, matrices):
    with open(filename, 'w') as file:
        for rows, columns, matrix in matrices:
            matrix_str = matrix_to_string(matrix)
            file.write(f"{rows}x{columns}:{matrix_str}\n")


def main():
    num_matrices = 110000
    num_duplicates = 70000

    matrices = []
    unique_matrices = set()

    while len(unique_matrices) < (num_matrices - num_duplicates):
        rows = random.randint(5, 10)
        columns = random.randint(5, 10)
        matrix = generate_matrix(rows, columns)
        matrix_str = matrix_to_string(matrix)
        unique_matrices.add((rows, columns, matrix_str))

    unique_matrices = list(unique_matrices)

    for rows, columns, matrix_str in unique_matrices:
        matrix = [[int(matrix_str[i * columns + j]) for j in range(columns)] for i in range(rows)]
        matrices.append((rows, columns, matrix))

    for _ in range(num_duplicates):
        rows, columns, matrix_str = random.choice(unique_matrices)
        matrix = [[int(matrix_str[i * columns + j]) for j in range(columns)] for i in range(rows)]
        matrices.append((rows, columns, matrix))

    random.shuffle(matrices)

    write_to_file('mat.in', matrices)


if __name__ == "__main__":
    main()
