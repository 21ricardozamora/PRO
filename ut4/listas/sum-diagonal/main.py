def run(matrix: list) -> int | None:
    size_matrix = min(len(matrix), len(matrix[0]))
    sum_diagonal = 0
    if size_matrix != len(matrix):
        sum_diagonal = None
    else:
        for i in range(size_matrix):
            sum_diagonal += matrix[i][i]

    return sum_diagonal


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
