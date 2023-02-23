
import utils

def get_pixel(img: list[list[int]], x: int, y: int) -> int:
    height = len(img)
    width = len(img[0])

    if x < 0 or x >= width:
        return 0
    elif y < 0 or y >= height:
        return 0
    else:
        return img[y][x]

def should_erode(img: list[list[int]], x: int, y: int) -> bool:
    # Relative positions to watch for neighbor
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    positions = [left, right, up, down]

    count = 0
    for dx, dy in positions:
        if get_pixel(img, x + dx, y + dy):
            count += 1
    # print("count", count)

    # pixel should be eroded if set to 1 and less than 4 neighbors are 1
    return get_pixel(img, x, y) == 1 and count < 4


def erosion(img: list[list[int]], n: int) -> list[list[int]]:
    height = len(img)
    width = height > 0 and len(img[0])
    # Création d'une liste de la bonne dimension pour
    # recevoir l'image destination
    img2 = [[0] * width for _ in range(height)]


    buffers = [img, img2]
    src, dest = 0, 1
    #print(buffers)
    for _ in range(n):
        for y, row in enumerate(buffers[src]):
            for x, col in enumerate(row):
                if should_erode(buffers[src], x, y):
                    # print('eroding pixel', x, y)
                    buffers[dest][y][x] = 0
                else:
                    buffers[dest][y][x] = buffers[src][y][x]
        src, dest = dest, src

    # comme on vient d'échanger src et dest, on retourne src
    # pour retourner le dernier buffer dans lequel on a écrit
    return buffers[src]