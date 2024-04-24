
# Park Ease

ParkEase is a computer vision project designed to automatically detect free parking spaces in video recordings. It leverages OpenCV libraries to process video frames and identify designated parking areas.


## Features

- Video Input: Processes video files to analyze parking space occupancy over time.
- Pre-defined ROIs: Utilizes pre-defined regions of interest (ROIs) to focus on specific parking space locations within the frame.
- Image Preprocessing: Applies grayscale conversion, Gaussian blur, adaptive thresholding, and median blur for noise reduction and image segmentation.
- Parking Space Analysis: Iterates through ROIs, extracts cropped images for each space, and analyzes pixel intensity to determine occupancy. A user-defined threshold is used to classify empty (green) and occupied (red) spaces.
- Visualization: Overlays text on the processed frame to display parking space numbers and occupancy status.

## Installation 

Import these Library Before Running

```bash

pip install opencv-python pickle cvzone pyqt5

```

## How to Run

```bash

Change Video and casPos file path to Your Local Video Path

```
Run the mainwithui.py file
```bash

python mainwithui.py

```



## Screenshots
Basic UI to run Program

![Basic UI](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/basicui.png)

Detecting Spaces in Video

![Space Detection](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/detectspace.png)

Creating Frames for every Spaces

![Make Frames](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/makeframe.png)

UI for User can see Free, Available, and Total Spaces 

![User UI](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/newuserui.png)

## Known Issues

1. Running create frame and detecting Spaces Crash the Program.
2. We can Open User UI without Detecting Spaces.

## Future Plans

1. Add a Database so we get real time parking space data any where any time.
2. Add a way to represent the Available, Occupied, Total Spaces in userui with its location and path to go there.
3. Improve overall ui and Clean the code.
