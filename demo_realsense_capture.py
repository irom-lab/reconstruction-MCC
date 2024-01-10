import pyrealsense2 as rs
import cv2
import numpy as np
import open3d as o3d
import IPython as ipy

# Get frame from realsense
align = rs.align(rs.stream.depth)
pipeline = rs.pipeline()
pipeline.start()
pc = rs.pointcloud()
frames = pipeline.wait_for_frames()
aligned = align.process(frames)
color_aligned_to_depth = aligned.first(rs.stream.color)

depth_frame = frames.first(rs.stream.depth)
points = pc.calculate(depth_frame)
w = rs.video_frame(depth_frame).width
h = rs.video_frame(depth_frame).height
verts = np.asanyarray(points.get_vertices()).view(np.float32).reshape(h, w, 3)
pipeline.stop()

# Color image
img = np.asanyarray(color_aligned_to_depth.get_data())

# Save point cloud using open3d
pcd = o3d.geometry.PointCloud()
xyz = verts.reshape((w*h,3))
pcd.points = o3d.utility.Vector3dVector(xyz)

verts_colors = img.reshape((w*h,3))
pcd.colors = o3d.utility.Vector3dVector(verts_colors/255)

o3d.io.write_point_cloud("./demo/test.ply", pcd)

# Save image
cv2.imwrite("./demo/test.jpg", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
