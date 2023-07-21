def print_triangle(size, character):
    """Function draw equilateral triangle"""
    triangle = ""
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        line = character * (2 * i - 1)
        if i == size:
         triangle += spaces + line
        else:   
         triangle += spaces + line + "\n"
    return triangle


if __name__ == '__main__':
    print(print_triangle(5, "*"))