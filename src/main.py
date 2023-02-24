
from utils import load_pbm, img2ascii

def erosion(img: list[list[int]], n: int) -> list[list[int]]:
    nb_line = len(img)
    nb_row = len(img[0])
    for i in range(n):
        copy_img = deepcopy(img)
        delete_first_last_line(i, img, nb_line, nb_row)
        # delete the first and last line and check all the other positions
        for elem_line in range(i + 1, nb_line - i - 1):
            img[elem_line][i] = 0
            img[elem_line][-1 - i] = 0
            check_positions(nb_row, i, elem_line, img, copy_img)
    return img
