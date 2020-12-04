# Image-Slice-and-Fuse
Python Project to pad, slice and fuse your Images.
This could be helpful to train large images in machine learning, which as a whole are too large for the memory of the hardware accelerator.

# Getting started:
## 1. Install required packages
They only required packages are numpy and Pillow.  
`pip install requirements.txt`

## 2. Slice and pad your Images
`python3 slice.py <source directory> <destination directory>`

## 3. Use images in training or execution

## 4. Fuse segmented images
`python3 fuse.py <source directory> <destination directory>`
