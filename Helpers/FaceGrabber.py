import sys
import os
import glob
import cv2
import numpy as np
# import dlib
import matplotlib.pyplot as plt

def FaceRip(folder='/content/portrait'):
    ''' 
        Rip all faces from a images folder
        Example:
            FaceRip(folder='/content/portrait')
    '''
    ''' Download and unzip the haar cascader '''
    predictor_file = ['shape_predictor_194_face_landmarks.zip','1fMOT_0f5clPbZXsphZyrGcLXkIhSDl3o']
    self.GdriveD.GdriveD(predictor_file[1],predictor_file[0])
    os.system('unzip /content/shape_predictor_194_face_landmarks.zip')

    ''' Detector predictor load'''
    predictor = predictor_file[0].replace('zip','dat')
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor)

    ''' glob the folder '''
    lst = HelpCore.GlobX(folder,'*.*g')

    ''' iterate of the images '''
    iter = 0
    for im in range(len(lst)-1):
        # load the image
        img = cv2.imread(lst[iter])

        # make grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect faces
        faces = detector(gray)

        # iterate over the faces
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            # cv2.rectangle(img, (x1-10, y1-10), (x2+10, y2+10), (0, 255, 0), 3) # draw rectangle on the image

            size_increase = 50 # increase size of face image output

            # save face without landmarkers
            res2 = img[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
            #grayscale of face
            res2_image_gray = gray[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]

            #save 
            os.makedirs(HelpCore.root+'/faces', exist_ok=True)
            cv2.imwrite(HelpCore.root+'/faces/face_img_'+str(iter)+'.jpg', res2)
            cv2.imwrite(HelpCore.root+'/faces/gray_face_img_'+str(iter)+'.jpg', res2_image_gray)

            # get thelandmarks of the face
            landmarks = predictor(gray, face)
            for n in range(0, 194):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(img, (x, y), 4, (255, 0, 100), -1)
                cv2.circle(gray, (x, y), 4, (255, 100, 0), -1)

            # face image
            res2 = img[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
            #grayscale face image
            res2_image_gray = gray[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]

            #save 
            os.makedirs(HelpCore.root+'/faces', exist_ok=True)
            cv2.imwrite(HelpCore.root+'/faces/landmark_face_img_'+str(iter)+'.jpg', res2)
            cv2.imwrite(HelpCore.root+'/faces/landmark_gray_face_img_'+str(iter)+'.jpg', res2_image_gray)
            
        # save total  
        os.makedirs(HelpCore.root + '/proc_images/total', exist_ok=True)
        cv2.imwrite(HelpCore.root + '/proc_images/total/img_'+str(iter)+'.jpg', img)
        cv2.imwrite(HelpCore.root + '/proc_images/total/gray_img_'+str(iter)+'.jpg', gray)
        iter += 1
