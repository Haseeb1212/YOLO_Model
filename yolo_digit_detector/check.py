import os
import cv2
import numpy as np


size=416
blank=np.ones((size,size,3),dtype=np.uint8)*255
path = os.path.join(os.getcwd(),"digit_cells")
images = os.listdir(path)
img = os.path.join(path,images[0])
pic = cv2.imread(img)
pic = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
# pic = cv2.cvtColor(pic,cv2.COLOR_GRAY2RGB)
(thresh, blackAndWhiteImage) = cv2.threshold(pic, 100, 255, cv2.THRESH_BINARY)
ker = np.ones((3,3))
ero = cv2.erode(blackAndWhiteImage,kernel=ker,iterations=1)

pic = cv2.cvtColor(ero,cv2.COLOR_GRAY2RGB)



x_offset=y_offset=50
blank[y_offset:y_offset+pic.shape[0], x_offset:x_offset+pic.shape[1]] = pic



cv2.imshow('das',blank)
cv2.waitKey(0)
cv2.destroyAllWindows()

