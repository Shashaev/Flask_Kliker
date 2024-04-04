from os.path import isfile


def save_image(image: bytes, path: str) -> None:
    with open(path, "bw") as f:
        f.write(image)


def is_image(path: str) -> bool:
    return isfile(path)
