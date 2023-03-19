

# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# print(pytesseract.image_to_string(r'D:\Srinu Docs\Images\1.png'))

# will convert the image to text string
import pytesseract 

# adds image processing capabilities
from PIL import Image   

 # opening an image from the source path
img = Image.open(r'D:\Srinu Docs\Images\1_png.png')

# describes image format in the output
# print(img)     

# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
# 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' 

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)   

#print(result)

# write text in a text file and save it to source path   
with open(r'D:\Srinu Docs\TextFiles\2.txt',mode ='w') as file: 
                 file.write(result)
                 print(result)



