from PIL import Image
from Slice.slicer import pad, img_slice
import os


IMG_PATH: str = "./Images/Original"
SLC_PATH: str = "./Images/Sliced"


def main():
    for file in os.listdir(IMG_PATH):
        if file.endswith(".jpg") or file.endswith(".png"):
            image = Image.open(os.path.join(IMG_PATH, file))
            image = pad(image, 384, 72)
            image_slices = img_slice(image, 2)
            for idx, image_slice in enumerate(image_slices):
                file_name: str = os.path.splitext(file)[0]
                file_ext: str = os.path.splitext(file)[1]
                image_slice.save(
                    os.path.join(SLC_PATH, file_name + f"_{idx}" + file_ext),
                    quality=100,
                    subsampling=0,
                )


if __name__ == "__main__":
    main()
