# feature precessing 
import cv2
import numpy as np
from skimage.transform import FundamentalMatrixTransform,EssentialMatrixTransform
from skimage.measure import ransac


<<<<<<< HEAD

def create_hmg(pts):
  'make the point homogenious point ' 
  n = pts.shape[0]
  return np.concatenate([pts,np.ones((n,1))],axis=1)

def normalize(K,pt):
      return np.dot(np.linalg(K),pt)[0:2,:]

=======
        self.K = K 
        self.Kinv = np.linalg.inv(self.K)
        
    def denormalize(self,pt):
        ret = pt[0]

        #ret = np.dot(self.Kinv,np.array([pt[0],pt[1],1.0]))
        #print(ret)
        #return (int(ret[0]),int(ret[1]))
    
    def extract(self,frame):
        features = cv2.goodFeaturesToTrack(np.mean(frame,axis = 2).astype(np.uint8),3000,qualityLevel = 0.01, minDistance = 7)
        
        # extraction method1
        kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in features]
        kps, des = self.orb.compute(frame,kps)
        
>>>>>>> d9844f33de3761dedf0138eeae8165c2b8436ea0


<<<<<<< HEAD

class extract_feature(object):

    def __init__(self,K):
      self.orb = cv2.ORB_create()
      self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
      self.last = None 
 
      self.K = K 
      self.Kinv = np.linalg.inv(self.K)
    
    def normalize(self,K,pt):
      return np.dot(np.linalg(K),pt)[0:2,:]
      

    
    def extract(self,frame,K):
      features = cv2.goodFeaturesToTrack(np.mean(frame,axis = 2).astype(np.uint8),3000,qualityLevel = 0.01, minDistance = 2)  
     
      kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in features]
      kps, des = self.orb.compute(frame,kps)
=======
        if len(good)> 0:
            good = np.array(good)
            
            # normalziation
            good[:,:,0] -= frame.shape[0]//2
            good[:,:,1] -= frame.shape[1]//2
            
            model,inliers = ransac((good[:,0],good[:,1]),
                FundamentalMatrixTransform,
                min_samples = 8,
                residual_threshold = 1,
                max_trials = 120)

            good = good[inliers]

            #only good mache about 700
            print('mached:',len(good))
>>>>>>> d9844f33de3761dedf0138eeae8165c2b8436ea0


      matches = None
      matching_pts = []
        
<<<<<<< HEAD
      # find matching points 
      bf = cv2.BFMatcher()
      if self.last != None:
        matches = bf.knnMatch(des,self.last['des'],k=2)
        
        for m,n in matches:
          if m.distance < 0.75*n.distance:
            kp1 = kps[m.queryIdx].pt
            kp2 = self.last['kps'][m.trainIdx].pt 
            matching_pts.append((kp1, kp2))
        
      if len(matching_pts)>0:
        matching_pts = np.array(matching_pts)

        # with the matching points, we find the "keymatching" points
        # from this ransac, we find the homography
        model,inliers = ransac((matching_pts[:,0],matching_pts[:,1]),FundamentalMatrixTransform,min_samples = 8,residual_threshold = 1,max_trials = 120)
          
        # this is better matching 'key' points
        matching_pts= matching_pts[inliers]
=======
        return np.array(good)
>>>>>>> d9844f33de3761dedf0138eeae8165c2b8436ea0
        

      self.last = {'kps':kps , 'des':des}
        
      return kps,np.array(matching_pts)
       




    
