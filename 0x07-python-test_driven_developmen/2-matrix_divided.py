def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with the divided elements, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row doesn't have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
        [[0.75, 1.25], [1.75, 2.25]]
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)
    return new_matrix
