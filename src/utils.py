import os

def img2ascii(
    img_data: list[list[int]],
    black: str = '#',
    white: str = '.'
) -> str:
    ...

def load_pbm(filename: str) -> list[list[int]]:
    ...


if __name__ == '__main__':
    import doctest
    doctest.testmod()

