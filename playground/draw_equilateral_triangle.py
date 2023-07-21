def print_triangle(size, character):
    """Function print triangle"""
    triangle = ""
    for row in range(1, size + 1):
        spaces = " " * (size - row)
        lines = character * (2 * row - 1)

        if row != size:
            triangle += spaces + lines + "\n"
        else:
            triangle += spaces + lines
    return triangle


if __name__ == '__main__':
    print(print_triangle(5, "*"))