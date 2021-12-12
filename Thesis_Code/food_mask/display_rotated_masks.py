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
    r'C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\datasets\MalteseFood_Dataset\train\IMG_7821_60.JPG')
r = rotate_image(image, 0)
cv2.imwrite('Mask_RCNN/Test.jpg', r)

# 1.) HERE WE ARE GETTING A BR VALUE FROM THE EXPORTED COCO VALUES AND TRANSFORMING THEM INTO A DRAWABLE POLYGON

BR = [ 1352, 1347, 1477, 1203, 1570, 1154, 1586, 1146, 1613, 1099, 1650,
            1066, 1697, 1051, 1730, 1049, 1765, 1064, 1837, 1099, 1893, 1117,
            1930, 1133, 2028, 1220, 2092, 1253, 2119, 1282, 2123, 1335, 2123,
            1493, 2107, 1631, 2121, 1689, 2127, 1722, 2127, 1749, 2111, 1775,
            2076, 1798, 2043, 1821, 1995, 1866, 1946, 1911, 1948, 1930, 1946,
            1944, 1921, 1960, 1882, 1977, 1781, 2006, 1747, 2032, 1707, 2043,
            1664, 2026, 1446, 1913, 1378, 1860, 1323, 1798, 1298, 1763, 1282,
            1703, 1292, 1574, 1302, 1506, 1319, 1483, 1317, 1426, 1329, 1378]
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

image_path = r'C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\food_mask\Mask_RCNN\Test.jpg'
image = Image.open(image_path)
draw = ImageDraw.Draw(image)
colors = ["red", "green", "blue", "yellow",
          "purple", "orange"]

# 1.) HERE WE CHECKING IF THE IMAGE IS LANDSCAPE OR PORTRAIT
# 2.) THEN WE USE THE ROTATE2D METHOD TO GET THE ROTATED VALUES
# 3.) FINALLY THE RETURN VALUE IS CONVERTED TO A TUPLE.

angle_degrees = 60
radian = mt.radians(angle_degrees)

w, h = image.size
if (w < h):
    ots = rotate2D(xy, sc.array([1224, 1632]), radian)
else:
    ots = rotate2D(xy, sc.array([1632, 1224]), radian)

ots_tuple = tuple(map(tuple, np.around(ots)))
draw.polygon(ots_tuple, fill=random.choice(colors))
image.show()
