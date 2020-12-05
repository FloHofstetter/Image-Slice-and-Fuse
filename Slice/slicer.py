from typing import Tuple, List
from PIL import Image
import numpy as np


def pad(image: Image.Image, vertically: int = 0, horizontally: int = 0) -> Image.Image:
    """
    Pad image equally on opposite sides.

    :param image: Image to be padded.
    :param horizontally: Pixels to pad in horizontal direction.
    :param vertically: Pixels to pad in vertical direction.
    :return: Padded Image
    """
    image_array: np.ndarray
    image_array = np.asarray(image)
    if image_array.ndim < 3:
        image_array = np.expand_dims(image_array, axis=2)
    pad_top: int = vertically // 2
    pad_left: int = horizontally // 2
    image_h: int
    image_w: int
    image_c: int
    image_h, image_w, image_c = image_array.shape
    padded_array: np.ndarray
    padded_array = np.zeros(
        shape=(image_h + horizontally, image_w + vertically, image_c), dtype="uint8"
    )
    padded_array[
        pad_left : pad_left + image_h, pad_top : pad_top + image_w, :
    ] = image_array
    if padded_array.shape[2] == 1:
        padded_array = padded_array.squeeze(axis=2)
    image = Image.fromarray(padded_array)
    return image


def img_slice(image: Image.Image, slices: int) -> List[Image.Image]:
    """
    Slice images in equal parts.

    :param image: Image to be sliced.
    :param slices: Amount of slices to produce.
    :return: List of image slices.
    """
    image_array: np.ndarray = np.asarray(image)
    image_h: int
    image_w: int
    if image_array.ndim < 3:
        image_array = np.expand_dims(image_array, axis=2)
    image_h, image_w, _ = image_array.shape
    array_slices: List[np.ndarray, ...] = []
    for slice_h in range(slices):
        for slice_v in range(slices):
            image_slice = image_array[
                (image_h // slices) * slice_v : (image_h // slices) * (slice_v + 1),
                (image_w // slices) * slice_h : (image_w // slices) * (slice_h + 1),
            ]
            if image_slice.shape[2] == 1:
                image_slice = image_slice.squeeze(axis=2)
            array_slices.append(image_slice)
    image_slices = [Image.fromarray(array_slice) for array_slice in array_slices]
    return image_slices


def main():
    pass


if __name__ == "__main__":
    main()
