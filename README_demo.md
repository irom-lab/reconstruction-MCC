# Installation

In addition to this repo, install `cv2` and `pyrealsense2`. 

Download the pretrained model checkpoint they make available. 

# Running the code
First collect a realsense image and point cloud:
```
python demo_realsense_capture.py
```

Next, use MeshLab to convert the saved ply file to an obj file (can probably also use open3d to do this).

Next, segment the image (you'll need to enter the pixel coordinates manually and check which of masks[0/1/2] works well):
```
python demo_segment.py
```

Finally, run:
```
python demo.py --image demo/test.jpg --point_cloud demo/test.obj --seg demo/test_seg.png --checkpoint co3dv2_all_categories.pth \
```
