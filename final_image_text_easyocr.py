
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image

import easyocr
reader = easyocr.Reader(['en'])


import PIL
from PIL import ImageDraw

image = PIL.Image.open(r'D:\Srinu Docs\Images\1.jpg')


bounds = reader.readtext(image)
#print(bounds)
draw = ImageDraw.Draw(image)

for bound in bounds:
    p0, p1, p2, p3 = bound[0]
    draw.line([*p0, *p1, *p2, *p3], fill='red', width=2)
    
plt.imshow(image)
# text = ''

# for i in range(len(bounds)):
#     text = text + bounds[i][1]

# print(text)
