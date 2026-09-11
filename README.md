# Color Object Detection

A small computer vision project I built while learning OpenCV.

The program uses my webcam to detect a green object in real time and draws a bounding box around the detected area.

## What I learned

- Working with OpenCV and webcam input
- Converting images from BGR to HSV
- Creating a color mask using `cv2.inRange()`
- Finding the bounding box of the detected region
- Using NumPy and Pillow with OpenCV

## How it works

1. Capture a frame from the webcam.
2. Convert the frame from BGR to HSV.
3. Create an HSV range for green.
4. Generate a binary mask for the selected color.
5. Find the bounding box of the detected region.
6. Draw the box on the original frame.

## Setup

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt