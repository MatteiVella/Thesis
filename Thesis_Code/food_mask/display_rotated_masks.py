import json
import random
import cv2
import numpy as np
import scipy as sc
import math as mt
from PIL import Image, ImageDraw


def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def rotate2D(pts, cnt, ang=sc.pi / 4):
    return sc.dot(pts - cnt, sc.array([[sc.cos(ang), sc.sin(ang)], [-sc.sin(ang), sc.cos(ang)]])) + cnt



image = cv2.imread(
    r'C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\datasets\MalteseFood_Dataset\train\IMG_7808.JPG')
r = rotate_image(image, -15)
cv2.imwrite('Mask_RCNN/Test.jpg', r)

# 1.) HERE WE ARE GETTING A BR VALUE FROM THE EXPORTED COCO VALUES AND TRANSFORMING THEM INTO A DRAWABLE POLYGON

BR = [2258.83, 430, 2258.427, 439.224, 2257.222, 448.377, 2255.224, 457.391, 2252.448, 466.196, 2248.915, 474.726,
      2244.651, 482.915, 2239.691, 490.702, 2234.07, 498.026, 2227.833, 504.833, 2221.026, 511.07, 2213.702, 516.691,
      2205.915, 521.651, 2197.726, 525.915, 2189.196, 529.448, 2180.391, 532.224, 2171.377, 534.222, 2162.224, 535.427,
      2153, 535.83, 2143.776, 535.427, 2134.623, 534.222, 2125.609, 532.224, 2116.804, 529.448, 2108.274, 525.915,
      2100.085, 521.651, 2092.298, 516.691, 2084.974, 511.07, 2078.167, 504.833, 2071.93, 498.026, 2066.309, 490.702,
      2061.349, 482.915, 2057.085, 474.726, 2053.552, 466.196, 2050.776, 457.391, 2048.778, 448.377, 2047.573, 439.224,
      2047.17, 430, 2047.573, 420.776, 2048.778, 411.623, 2050.776, 402.609, 2053.552, 393.804, 2057.085, 385.274,
      2061.349, 377.085, 2066.309, 369.298, 2071.93, 361.974, 2078.167, 355.167, 2084.974, 348.93, 2092.298, 343.309,
      2100.085, 338.349, 2108.274, 334.085, 2116.804, 330.552, 2125.609, 327.776, 2134.623, 325.778, 2143.776, 324.573,
      2153, 324.17, 2162.224, 324.573, 2171.377, 325.778, 2180.391, 327.776, 2189.196, 330.552, 2197.726, 334.085,
      2205.915, 338.349, 2213.702, 343.309, 2221.026, 348.93, 2227.833, 355.167, 2234.07, 361.974, 2239.691, 369.298,
      2244.651, 377.085, 2248.915, 385.274, 2252.448, 393.804, 2255.224, 402.609, 2257.222, 411.623, 2258.427, 420.776]
x = []
y = []
xy = []

no_coords = (len(BR) / 2)

num = 0
num2 = 1
counter = 0

# HERE WE ARE BUILDING THE BR ARRAY WHICH IS MADE UP OF THIS FORMAT : x1,y1,x2,y2,x3,y3 etc...
# THIS IS BEING TRANSFORMED INTO THIS FORMAT : (x1,y1),(x2,y2)

for i in range(int(no_coords)):
    x.insert(counter, BR[num])
    y.insert(counter, BR[num2])
    num = num + 2
    num2 = num2 + 2
    counter = counter + 1

counter = 0
for z in range(int(no_coords)):
    temp_x = x[counter]
    temp_y = y[counter]
    xy.insert(counter, [temp_x, temp_y])
    counter = counter + 1

image_path = r'C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\food_mask\Test.jpg'
image = Image.open(image_path)
draw = ImageDraw.Draw(image)
colors = ["red", "green", "blue", "yellow",
          "purple", "orange"]

# 1.) HERE WE CHECKING IF THE IMAGE IS LANDSCAPE OR PORTRAIT
# 2.) THEN WE USE THE ROTATE2D METHOD TO GET THE ROTATED VALUES
# 3.) FINALLY THE RETURN VALUE IS CONVERTED TO A TUPLE.

angle_degrees = 15
radian = mt.radians(angle_degrees)

w, h = image.size
if (w < h):
    ots = rotate2D(xy, sc.array([1224, 1632]), radian)
else:
    ots = rotate2D(xy, sc.array([1632, 1224]), radian)

ots_tuple = tuple(map(tuple, ots))
draw.polygon(ots_tuple, fill=random.choice(colors))
image.show()
