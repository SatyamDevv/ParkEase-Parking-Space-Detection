import cv2
import pickle

#video capture object
cap = cv2.VideoCapture('D:\Christ\SEMESTER 4\DBMS Project\ParkEase\carPark2.mp4')

try:
    with open('D:\Christ\SEMESTER 4\DBMS Project\CarParkPos1', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    
width, height = 80, 180    

#this funtion make rectange on the video
def mouseClick(events, x, y, flags, params):
    
    #add rectangle on the video by left click on the video
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    
    #this delete the rectangle on the video by right click on the rectangle
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
                
    
    #this write the coordinates of the rectangle in the file    
    with open('CarParkPos1', 'wb') as f:  
        pickle.dump(posList, f)  

    #test code
    
    #test code

def runframes():
 while True:
    #get frames
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    #img = cv2.imread('D:\Christ\SEMESTER 4\DBMS Project\ParkEase\carParkImg3resize.png')  
    success, img = cap.read() 
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, (pos[1]+height)), (0, 0, 100), 2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    keyCode = cv2.waitKey(1)
    if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) <1:
        break

    

#runframes()


#cv2.rectangle(img, (750, 690), (630, 450), (0, 0, 100), 2)
#right side and lower down = (➡️,⬇️) | left side and upper down (➡️,⬇️)