from typing import List, Callable
from PIL import Image
import numpy as np


def fuse(
    images: List[Image.Image], height_fused: int = 576, width_fused: int = 1152
) -> Image.Image:
    """
    Get a list of images and return the fused image.

    :param images: List of images.
    :param height_fused: Height of fused image.
    :param width_fused: Width of fused image.
    :return: Fused image.
    """
    image: Image.Image = images[0]
    image_array: np.ndarray = np.asarray(image)
    image_shape: list = list(image_array.shape)
    len_images: int = len(images)
    image_shape[0] = image_shape[0] * int(np.sqrt(len(images) + 1))
    image_shape[1] = image_shape[1] * int(np.sqrt(len(images) + 1))
    fused_image_array = np.zeros(image_shape, dtype="uint8")
    # print(fused_image_array.shape)

    img_nr = 0
    for w in range(int(np.sqrt(len(images)))):
        for h in range(int(np.sqrt(len(images) + 1))):
            fused_image_array[
                height_fused * h : height_fused * (h + 1),
                width_fused * w : width_fused * (w + 1),
            ] = np.asarray(images[img_nr])
            img_nr += 1

    fused_image: Image.Image = Image.fromarray(fused_image_array)
    return fused_image


def main():
    pass


if __name__ == "__main__":
    main()
