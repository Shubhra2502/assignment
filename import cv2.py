import cv2
import numpy as np

def extract_image_one_fps(video_source_path):

    vidcap = cv2.VideoCapture("/Users/shubhrasaxena/Downloads/tom and jerry.mp4")
    count = 0
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))      
      success,image = vidcap.read()

      ## Stop when last frame is identified
      image_last = cv2.imread("frame{}.png".format(count-1))
      if np.array_equal(image,image_last):
          break

      cv2.imwrite("frame%d.png" % count, image)     # save frame as PNG file
      print '{}.sec reading a new frame: {} '.format(count,success)
      count += 1