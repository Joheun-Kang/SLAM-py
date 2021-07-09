

python slam implementation for short videos
=======
# Simultaneous Localization and Mapping (SLAM)
## mini_SLAM (In Progress, update: 7/7/2021)


Python SLAM implementation for short videos

## Slam Process 
=======
## example video capture 
![video_capture1](https://user-images.githubusercontent.com/57236540/124831382-fada4e80-df2f-11eb-84f1-ff4865319f04.png)





## Features: 
1. kps: keypoints 
2. descriptor: The local appreance around each feature point is described in some way invariant under changes in iillumination, translation, scale, and in-plane rotation. we get descriptor vector for each feature point

descriptors are compared across the images, to identify similar features. 

## Overview of the process

0. find matching keypoints (frame by frame)
1. update the current state estimate using the keypoints.
2. update the estimated state from re-observing landmarks

1. find matching keypoints (frmae by frame )
2. display 2d matching points on each frame

Todo:
1. update the current state estimate using the odometry data
2. update the estimated state from re-observing landmarks
3. Add new landmarks to the current state 



## Variables

1. goodFeaturesToTrack

cv.goodFeaturesToTrack(	image, maxCorners, qualityLevel,
                          minDistance[, corners[, mask[,
                          blockSize[, useHarrisDetector[, k]]]]]	) ->	corners

: finds the most prominent corners in the image. 
: can be used to initialize a point-based tracker of an object 

<<<<<<< HEAD
## Camera position
-  np.eye(n):
Return a 2D array with ones on the diagonal and zeros elsewhere.
=======


## Camera position (TODO)



- Homography (cv2.findHomography)
resource:https://learnopencv.com/homography-examples-using-opencv-python-c/

A transformation (a 3 by 3 matrix) that maps the points in one image to the corresponding points in the other image.




- IntrinsicMatrix
https://ksimek.github.io/2013/08/13/intrinsic/ (instrinsic matrix explanation)
https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/2881135-intrinsicmatrixhe 

intrinsic matrix (commonly represented in equations as K) allows you to transform 3D coordinates to 2D coordinates on an image plane using the pinhole camera model.

1. Focal length (f_x,f_y)
TODO: 
-how to find focal length? 
=======
- Focal length (f_x,f_y)

- Principal Point Offset (x0,y0)
The camera's "principal axis" is the line perpendicular to the image plane that passes through the pinhole. Its itersection with the image plane is referred to as the "principal point". 


- Cameral Focal Length



2. Principal Point Offset (x0,y0)
The camera's "principal axis" is the line perpendicular to the image plane that passes through the pinhole. Its itersection with the image plane is referred to as the "principal point". 
  
 x0 = w//2
 x1 = h//2 

notsure: 
https://learnopencv.com/camera-calibration-using-opencv/
retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(objectPoints, imagePoints, imageSize)


3. Camera Projection Matrix
Very good resource!                                                                        
https://www.cc.gatech.edu/classes/AY2016/cs4476_fall/results/proj3/html/jhan320/index.html 


GOAL: calculate camera center with the projection matrix 
THOUGHTS: I think intrinsicMatrix isthe [3x3] parts of the camera projection matrix 
projection matrix (4x4) , 3D coordinate (4 by 1) results in 2D image coordinates to some scale.

To resolve that issue, the last element of the projection matrix was fixed to 1, and the remaining coefficients were then calculated. Thus, the resulting projection matrix was scaled based on the hard-coded value of the last element in the projection matrix.

from that projection matrix, the camera center in world coordinates was estimated. 
The projection matrix M can be split into a 3x3 matrix called Q and the final 3x1 vector that is called m4 (since it is the fourth column of the matrix).

The camera center can then be calculated by doing the dot product between negative Q inverse and m4.

4. Fundamental Matrix Estimation
what is fundamental matrix for ?
: relates correspoinding points between a pair of uncalibrated images. The matrix transforms homogeneous image points in one image to epipolar lines in the other image.

Uncalibrated: intrinsic calibration (focal lengths, pixel skew, principal point) of the two cameras is not known.


5. Point Normalization

# SLAM-implementation
