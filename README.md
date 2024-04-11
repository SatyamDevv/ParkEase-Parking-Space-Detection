
# Park Ease

ParkEase is a computer vision project designed to automatically detect free parking spaces in video recordings. It leverages OpenCV libraries to process video frames and identify designated parking areas.


## Features

- Video Input: Processes video files to analyze parking space occupancy over time.
- Pre-defined ROIs: Utilizes pre-defined regions of interest (ROIs) to focus on specific parking space locations within the frame.
- Image Preprocessing: Applies grayscale conversion, Gaussian blur, adaptive thresholding, and median blur for noise reduction and image segmentation.
- Parking Space Analysis: Iterates through ROIs, extracts cropped images for each space, and analyzes pixel intensity to determine occupancy. A user-defined threshold is used to classify empty (green) and occupied (red) spaces.
- Visualization: Overlays text on the processed frame to display parking space numbers and occupancy status.

## How to Run

Import these Library Before Running

```bash

pip install opencv-python pickle cvzone pyqt5

```

```bash

Change Video Path to Your Local Video Path

```

```bash

Run mainwithui.py File

```



## Screenshots

![Basic UI](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/basicui.png)

![Space Detection](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/detectspace.png)

![Make Frames](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/makeframe.png)

![User UI](https://github.com/SatyamDevv/ParkEase-Parking-Space-Detection/blob/main/Screenshots/userui.png)

