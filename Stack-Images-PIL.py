# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:41:15 2022

@author: dilan
"""

import os, numpy, PIL
from PIL import Image

# Access all PNG files in directory
#allfiles=os.listdir(os.getcwd())
os.chdir("black/t")
allfiles=os.listdir()
imlist=[filename for filename in allfiles if  filename[-4:] in [".bmp",".BMP"]]
print("File list = ", imlist)
print()

# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(imlist[0]).size
N=len(imlist)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,1),float)

# Build up average pixel intensities, casting each image as an array of floats
for im in imlist:
    print("Current file: ", im)
    imarr=numpy.array(Image.open(im),dtype= float)
    arr = numpy.mat(arr) + numpy.mat(imarr / N)

# Round values in array and cast as 8-bit integer
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

# Generate, save and preview final image
#out=Image.fromarray(numpy.mat(arr),mode="GREY")
out = Image.fromarray(numpy.mat(arr))
out.save("Average.png")
out.show()