from typing import Tuple
from PIL import Image
from Slice.slicer import pad, img_slice
import os
import sys


def main():
    img_path: str = sys.argv[1]
    slc_path: str = sys.argv[2]
    padding: Tuple[int] = (int(sys.argv[3]), int(sys.argv[4]))
    slices: int = int(sys.argv[5])

    for file in os.listdir(img_path):
        if file.endswith(".jpg") or file.endswith(".png"):
            image = Image.open(os.path.join(img_path, file))
            image = pad(image, *padding) # 384, 72
            image_slices = img_slice(image, slices)
            for idx, image_slice in enumerate(image_slices):
                file_name: str = os.path.splitext(file)[0]
                file_ext: str = os.path.splitext(file)[1]
                image_slice.save(
                    os.path.join(slc_path, file_name + f"_{idx}" + file_ext),
                    quality=100,
                    subsampling=0,
                )


if __name__ == "__main__":
    main()
