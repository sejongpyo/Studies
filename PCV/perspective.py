import numpy as np
import cv2

coordi = []

def get_coordinates(event, x, y, flags, params):
    '''
    get coordinates of an image by clicking points
    '''
    global coordi
    
    if event == cv2.EVENT_LBUTTONDOWN:
        coordi.append([x, y])
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('image', img)

    # elif event == cv2.EVENT_RBUTTONDOWN:




img= cv2.imread('museum.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', get_coordinates)
cv2.waitKey(0)
coor = np.float32(coordi)

# height = np.max(coor[:, 1]) - np.min(coor[:, 1])
# width = np.max(coor[:, 0]) - np.min(coor[:, 0])

width = np.linalg.norm(coor[1] - coor[0])
height = np.linalg.norm(coor[2] - coor[0])

move = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

M = cv2.getPerspectiveTransform(coor, move)
dst = cv2.warpPerspective(img, M, (width, height))
cv2.imshow('dst', dst)


cv2.waitKey(0)

cv2.destroyAllWindows()