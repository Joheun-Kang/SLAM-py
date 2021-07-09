import paths
import numpy as np
import imutils
import cv2


def distance_to_camera(knownWidth, f, picWidth):
  return (knownWidth*f) / picWidth

image = cv2.imread('imgs/img1.jpeg')
cv2.imshow('image', image)
marker = cv2.selectROI('image',image,fromCenter= False, showCrosshair = True)

picWidth = marker[2]


