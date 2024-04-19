import cv2
import pickle
import cvzone
import numpy as np
import ctypes

# Video capture
cap = cv2.VideoCapture(r'C:\Users\satya\OneDrive\Documents\GitHub\ParkEase-Parking-Space-Detection\carPark2.mp4') #change this according to your video path

# Load rectangle box positions
with open(r'C:\Users\satya\OneDrive\Documents\GitHub\ParkEase-Parking-Space-Detection\CarParkPos1', 'rb') as f: #change this according to your pickle file path
    posList = pickle.load(f)

width, height = 80, 180

# Create a shared variable for spaceCounter
shared_space_counter = ctypes.c_int(0)

def checkParkingSpace(imgPro, img):
    spaceCounter = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x, y+height-1), scale=1.5, thickness=2, offset=0, colorR=(0, 200, 0))
        cvzone.putTextRect(img, str(posList.index(pos)), (x, y+15), scale=1.5, thickness=2, offset=0, colorR=(0, 200, 0))
        if count < 1500:
            color = (0, 255, 0)
            thickness = 2
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0]+width, (pos[1]+height)), color, thickness)
    cvzone.putTextRect(img, f'Free Space: {str(spaceCounter)}/{len(posList)}', (100, 50), scale=2, thickness=2, offset=20, colorR=(0, 200, 0))
    return spaceCounter

def update_space_counter(spaceCounter):
    shared_space_counter.value = spaceCounter

def determineSpot():
    while True:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernal = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernal, iterations=1)
        spaceCounter = checkParkingSpace(imgDilate, img)
        update_space_counter(spaceCounter)  # Update the shared variable
        cv2.imshow("Image", img)
        #cv2.imshow("imgBlur",imgBlur)
        #cv2.imshow("imgThreshold",imgThreshold)
        #cv2.imshow("imgMedian",imgMedian)
        #cv2.imshow("imgDilate", imgDilate)
        keyCode = cv2.waitKey(1)
        if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
    
#determineSpot()