#
print("Hello")

#
from PIL import Image 
import numpy as np   #Use numpy to convert images to arrays

#
# Read image 
img = Image.open("/content/BB.jpg") #Not a numpy array
print(type(img))

#
# prints format of image 
print(img.format) 

#
# prints mode of image 
print(img.mode) 

#PIL is not by default numpy array but can convert PIL image to numpy array. 
img1 = np.asarray(img)
print(type(img1))

#
img1

#
img1.shape

#
print(img1.shape)

#
img = Image.open("/content/BB.jpg") #Not a numpy array
print(type(img))

#
img2.shape

#
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 

img = mpimg.imread("/content/BB.jpg")  #this is a numpy array
print(type(img))
#print(img)

print(img.shape)

plt.imshow(img)
plt.colorbar()

#
from skimage import io, img_as_float, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt 


image = img_as_float(io.imread("/content/BB.jpg"))

image2 = io.imread("/content/roman.jpg").astype(np.float)

print(image2)

#
import cv2  # library for Open Source Computer vision library

from google.colab.patches import cv2_imshow

grey_img = cv2.imread("/content/roman.jpg", 1)
color_img = cv2.imread("/content/BB.jpg", 0)

#images opened using cv2 are numpy arrays
print(type(grey_img)) 
print(type(color_img))

#
cv2_imshow(grey_img)
cv2_imshow(color_img)

#
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))

#
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV))

#
import numpy as np       # library used for working with arrays
import matplotlib.pylab as plt  # library used for ploting, graph
from io import BytesIO
import cv2  # library for Open Source Computer vision library
from PIL import Image    # Python Imaging Library for load, display, save etc
from google.colab.patches import cv2_imshow
from google.colab import files
uploaded = files.upload()

#
img1=Image.open(BytesIO(uploaded['roman.jpg']))
img2 = cv2.imread("roman.jpg")

#
gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#
[rows,cols] = gray_img.shape;
neg_img = np.zeros((rows,cols));
for r in range(0, rows-1):
  for c in range(0, cols-1):
    neg_img[r,c] = 255-gray_img[r,c]; #Calculate negative image
#plt.imshow(neg_img, cmap=plt.cm.gray)
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img1)
ax1.set_title('Original image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(gray_img, cmap=plt.cm.gray)
ax2.set_title('Gray image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(neg_img)
ax3.set_title('Negative image')

#
c = 255/(np.log(1 + np.max(gray_img))) 
log_transformed = c * np.log(1 + gray_img)
log_transformed1 = np.array(log_transformed, dtype = np.uint8)
plt.imshow(log_transformed1, cmap=plt.cm.gray)

#
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img1)
ax1.set_title('Original image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(gray_img, cmap=plt.cm.gray)
ax2.set_title('Gray image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(neg_img, cmap=plt.cm.gray)
ax3.set_title('Negative')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(log_transformed1, cmap=plt.cm.gray)
ax4.set_title('Log image')



