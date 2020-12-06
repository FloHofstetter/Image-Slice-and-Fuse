from typing import List, Callable
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt


def fuse(images: List[Image.Image]) -> Image.Image:
    """
    Get a list of images and return the fused image.

    :param images: List of images.
    :return: Fused image.
    """
    image: Image.Image = images[0]
    image_array: np.ndarray = np.asarray(image)
    image_shape: list = list(image_array.shape)
    len_images: int = len(images)
    image_shape[0] = image_shape[0] * int(np.sqrt(len(images)+1))
    image_shape[1] = image_shape[1] * int(np.sqrt(len(images)+1))
    fused_image_array = np.zeros(image_shape, dtype="uint8")
    # print(fused_image_array.shape)

    img_nr = 0
    for w in range(int(np.sqrt(len(images)))):
        for h in range(int(np.sqrt(len(images)+1))):
            # plt.imshow(images[img_nr])
            # plt.show()
            # print(f"H: {576 * h} {576*(h+1)} W: {1152 * w} {1152*(w+1)}")
            fused_image_array[
                576 * h : 576 * (h + 1), 1152 * w : 1152 * (w + 1)
            ] = np.asarray(images[img_nr])
            img_nr += 1

    fused_image: Image.Image = Image.fromarray(fused_image_array)
    return fused_image


def main():
    SLC_PATH: str = "../Images/Sliced"
    FUS_PATH: str = "../Images/Fused"

    sliced_image_paths=[]
    for file in os.listdir(SLC_PATH):
        if file.endswith(".jpg") or file.endswith(".png"):
            sliced_image_paths.append(os.path.join(SLC_PATH, file))
    # Sort files by slice index
    sort_key: Callable = lambda f: int(f.split("_")[-1].split(".")[-2])
    sliced_image_paths = sorted(sliced_image_paths, key=sort_key)

    print(sliced_image_paths)
    sliced_images = []
    for image_path in sliced_image_paths:
        sliced_images.append(Image.open(image_path))

    fused_name = lambda n: "_".join(n.split("_")[:-1]) + "." + n.split(".")[-1]
    fused_image = fuse(sliced_images)
    fused_image.save(os.path.join(FUS_PATH, fused_name(file)), quality=100, subsampling=0)


if __name__ == "__main__":
    main()
