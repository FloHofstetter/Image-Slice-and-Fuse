from typing import List, Callable
from PIL import Image
import Fusion.fuser
import os
import sys


def main():
    slc_path: str = sys.argv[1]
    fus_path: str = sys.argv[2]

    sliced_image_paths: List[str] = []
    for file in os.listdir(slc_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            sliced_image_paths.append(os.path.join(slc_path, file))

    # Sort files by slice index
    sort_key: Callable = lambda f: int(f.split("_")[-1].split(".")[-2])
    sliced_image_paths: str = sorted(sliced_image_paths, key=sort_key)

    sliced_images: List[Image.Image] = []
    for image_path in sliced_image_paths:
        sliced_images.append(Image.open(image_path))

    fused_name: Callable
    fused_name = lambda n: "_".join(n.split("_")[:-1]) + "." + n.split(".")[-1]
    fused_image: Image.Image = Fusion.fuse(sliced_images)
    fused_image.save(os.path.join(fus_path, fused_name(file)), quality=100, subsampling=0)


if __name__ == "__main__":
    main()
