from segment_anything import SamPredictor, sam_model_registry
import matplotlib.pyplot as plt
import numpy as np
import cv2
import IPython as ipy

sam = sam_model_registry["default"](checkpoint="sam_vit_h_4b8939.pth")
predictor = SamPredictor(sam)

# Image
img = plt.imread("./demo/test.jpg")
# img = np.uint8(img*255)
predictor.set_image(img)

plt.imshow(img); plt.show()

# Segmentation prompt
input_point = np.array([[401, 239]])
input_label = np.array([1])

masks, scores, logits = predictor.predict(
    point_coords=input_point,
    point_labels=input_label)

ipy.embed()

plt.imshow(masks[2]); plt.show()

# Write mask image
cv2.imwrite("./demo/test_seg.png", 1*masks[2])

