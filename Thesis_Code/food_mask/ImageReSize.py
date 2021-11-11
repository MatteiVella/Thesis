# Importing Image class from PIL module
import sys
from PIL import Image

# Opens a image in RGB mode
for x in range(1, 2):

    fixed_height = 3264
    image = Image.open(r'C:\Users\matte\OneDrive\Desktop\Thesis\Thesis_Code\datasets\MalteseFood_Dataset\IMG_781'+str(x)
                    + '.jpg')
    print(image.size[0], image.size[1])
    height_percent = (fixed_height / float(image.size[0]))
    width_size = int((float(image.size[1]) * float(height_percent)))
    image = image.resize((2448, fixed_height), Image.NEAREST)
    image.save('resized_nearest.jpg')