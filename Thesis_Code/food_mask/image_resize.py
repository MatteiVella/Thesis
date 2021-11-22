# Importing Image class from PIL module
import sys
from PIL import Image

import cv2
import os

relevant_path = r"C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\datasets\MalteseFood_Dataset\val"
included_extensions = ['JPG']
print(os.listdir(relevant_path))
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]

for name in file_names:

    img = cv2.imread('C://Users//matte//OneDrive//Desktop//Thesis//Thesis_Code//datasets//MalteseFood_Dataset//val//' + name)
    scale_percent = 0.81
    dim_size = (round(img.shape[1]*scale_percent), round(img.shape[0]*scale_percent) )
    new_img = cv2.resize(img, dim_size, interpolation=cv2.INTER_AREA)

    cv2.imwrite(name, new_img)