from PIL import Image
import numpy as np


def pad(image: Image.Image, horizontally: int = 0, vertically: int = 0) -> Image.Image:
    """
    Pad image equally on opposite sides.

    :param image: Image to be padded.
    :param horizontally: Pixels to pad in horizontal direction.
    :param vertically: Pixels to pad in vertical direction.
    :return: Padded Image
    """
    image_array: np.ndarray
    image_array = np.asarray(image)
    pad_left: int = vertically // 2
    pad_top: int = horizontally // 2
    image_h: int
    image_w: int
    image_c: int
    image_h, image_w, image_c = image_array.shape
    padded_array: np.ndarray
    padded_array = np.zeros(
        shape=(image_h + vertically, image_w + horizontally, image_c), dtype="uint8"
    )
    padded_array[
        pad_left : pad_left + image_h, pad_top : pad_top + image_w, :
    ] = image_array
    image = Image.fromarray(padded_array)
    return image


def main():
    image = Image.open("../Images/Original/rs01001.jpg")
    image = pad(image, 72, 384)
    image.save("../Images/Padded/rs01001.jpg", quality=100, subsampling=0)


if __name__ == "__main__":
    main()
