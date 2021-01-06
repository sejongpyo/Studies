import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('/Users/sejongpyo/downloads/yubi.jpg')
img = cv2.resize(img, (300, 500))

cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 20, nothing)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K', 'image')
    
    # (0, 0)은 에러 발생으로 1로 변환
    if k == 0:
        k = 1
        
    # by trackbar -> (1, 1) ~ (20, 20) kernel
    kernel = np.ones((k, k), np.float32)/(k*2)
    dst = cv2.filter2D(img, -1, kernel)
    
    cv2.imshow('image', dst)
cv2.destoryAllWindows()