"""
Header: UW 2017 - Intro To Python
Topic: Drawing Grid
Author: PydPiper

Objective: Print a row:X by col:X grid with variable size as well, example:
            a 2 by 3 by 2 would be
            +--+--+--+
            |  |  |  |
            |  |  |  |
            +--+--+--+
            |  |  |  |
            |  |  |  |
            +--+--+--+
"""

def draw_grid(row: int = 2, col: int = 2, size: int = 2) -> str:
    """
    Prints a grid of variable row/col/size, corner = "+", horizontal = "-", vertical = "|" ends.

    :param row: (type: int, default = 2)
    :param col: (type: int, default = 2)
    :param size: (type: int, default = 2)
    :return: (type: str) a printable string representation of the output grid
    """

    mem_horiz = "-"
    mem_vert = "|"
    mem_end = "+"
    mem_empt = " "

    # "+--"
    top = mem_end + mem_horiz * size
    # "|  "
    side = mem_vert + mem_empt * size

    rv = ""

    # add tops "row" times
    for _ in range(row):
        # "+--" times col and "+" to close it out
        rv += top * col + mem_end + "\n"
        # add sides "size" times
        for _ in range(size):
            # "|  " times col and "|" to close it out
            rv += side * col + mem_vert + "\n"
    # add close out the bottom
    rv += top * col + mem_end

    return rv


if __name__ == "__main__":
    print(draw_grid(10,10,1))
