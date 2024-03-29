'''
    face detection using haar cascades
    Usage:
        facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''
from __future__ import print_function
import numpy as np
import cv2 as cv
from video import create_capture
from common import clock, draw_str
class Haar_Detect():
  def detect(img, cascade):
      rects = cascade.detectMultiScale(img, 
                                       scaleFactor=1.3, 
                                       minNeighbors=4, 
                                       minSize=(30, 30),
                                       flags=cv.CASCADE_SCALE_IMAGE)
      if len(rects) == 0:
          return []
      rects[:,2:] += rects[:,:2]
      return rects

  def draw_rects(img, rects, color):
      for x1, y1, x2, y2 in rects:
          cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

  def main():
      import sys

      cascade_fn = "data/haarcascades/haarcascade_frontalface_alt.xml"
      nested_fn  = "data/haarcascades/haarcascade_eye.xml"
      cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))
      nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))
      cam = create_capture(video_src, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('samples/data/lena.jpg')))
      while True:
          ret, img = cam.read()
          gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
          gray = cv.equalizeHist(gray)
          t = clock()
          rects = detect(gray, cascade)
          vis = img.copy()
          draw_rects(vis, rects, (0, 255, 0))
          if not nested.empty():
              for x1, y1, x2, y2 in rects:
                  roi = gray[y1:y2, x1:x2]
                  vis_roi = vis[y1:y2, x1:x2]
                  subrects = detect(roi.copy(), nested)
                  draw_rects(vis_roi, subrects, (255, 0, 0))
          dt = clock() - t
          draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
          cv.imshow('facedetect', vis)
          if cv.waitKey(5) == 27:
              break
      print('Done')    
