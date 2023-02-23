import os

def img2ascii(
    img_data: list[list[int]],
    black: str = '#',
    white: str = '.'
) -> str:
    return '\n'.join(
        ''.join(black if pixel else white for pixel in row)
        for row in img_data
    )

def load_pbm(filename: str) -> list[list[int]]:
    # image data
    magic_code = ''
    width = 0
    height = 0

    # grid of pixels, indexed by pixels[row][col]
    pixels: list[list[int]] = [[]]
    
    print(f'loading {os.path.abspath(filename)}')

    with open(filename, 'r') as imagefile:
        lineno = 1

        # pixel count
        pixel_counter = 0
        # row and column index
        row, col = 0, 0

        for line in imagefile:
            line = line.strip()
            if line.startswith('#'):
                continue

            if lineno == 1:
                magic_code = line
            elif lineno == 2:
                width, height = [int(x) for x in line.split(' ')]
                pixels = [[0] * width for _ in range(height)]
                # print(width, height)
            else:
                # its a pixel data line
                for pixel in line:
                    if pixel == ' ':
                        continue

                    try:
                        pixels[row][col] = int(pixel)
                    except Exception as e:
                        print(f"Error : {e}. row={row}, col={col}, pixel={pixel}")
                        break

                    pixel_counter += 1
                    col += 1

                    if col >= width:
                        col = 0
                        row += 1

            lineno += 1
    return pixels


if __name__ == '__main__':
    import doctest
    doctest.testmod()

