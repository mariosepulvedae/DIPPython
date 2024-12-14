"""
Created on Fri Dec 13 22:35:18 2024

@author: Mario Eduardo Sepúlveda Hernández
"""
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

imagenA=cv.imread("brain.jpg")
imagenA=cv.cvtColor(imagenA, cv.COLOR_BGR2GRAY)
imagenA=np.asarray(imagenA)
negative=255-imagenA



plt.subplot(1,2,1)
plt.imshow(imagenA,cmap="gray")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")
plt.title(label="Brain tomography")

plt.subplot(1,2,2)
plt.imshow(negative,cmap="gray")
plt.title(label="Negative of the original image")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")

plt.show
plt.savefig("exampleNegative.jpg",dpi=500)
