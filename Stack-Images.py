# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:59:22 2022

@author: dilan

Horizontal and verticle average graphs added
subplot2grid added
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
#from matplotlib import gridspec
import seaborn as sns
#import load_file      # python script to load file
from itertools import chain # flattern list
from copy import copy, deepcopy
from textwrap import wrap

path = 'img-1-rot.png'

# set operating parameters here
# define squares to highlight the defect
x_square = 16
y_square = 20
overlap = 1


#lines to remove from average
#nlines_top = 3
#nlines_bot = 0
nlines_top = 0
nlines_bot = 0

# load image and calculate some parameters
img = cv2.imread(path, 0)
sy,sx = img.shape
plt.imshow(img, cmap="gray")
plt.show()