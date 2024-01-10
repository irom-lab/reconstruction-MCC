# Installation

In order to run the demo with the RealSense, you can install `cv2`,  `pyrealsense2`, and `SegmentAnything`. Alternately, you can use the test image from the RealSense provided in the demo folder. 

Download the pretrained model checkpoint MCC makes available. 

# Running the code

## Optional: collect RealSense data

First collect a realsense image and point cloud:
```
python demo_realsense_capture.py
```

Next, use MeshLab to convert the saved ply file to an obj file (can probably also use open3d to do this).

Next, segment the image (you'll need to enter the pixel coordinates manually and check which of masks[0/1/2] works well):
```
python demo_segment.py
```

## Run shape/scene completion

Run:
```
python demo.py --image demo/test.jpg --point_cloud demo/test.obj --seg demo/test_seg.png --checkpoint co3dv2_all_categories.pth
```

This will save an html file demo/output.html that you can use to visualize the completed shape. 

# Notes

This repo currently doesn't make the pretrained model from HyperSim available. This is required to do scene completion (rather than shape completion). But we can train this ourselves with their code. 
