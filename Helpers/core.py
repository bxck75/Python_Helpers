# -*- coding: utf-8 -*-

import os, sys, inspect
import numpy as np
import cv2
import dlib
import matplotlib.pyplot as plt

from . import ZipUp
from . import BigHelp
from . import RepCoList
from . import resize
from . import GdriveD
from . import logger
from . import GoImgScrape
from . import ColorPrint
from . import gscrape
from . import ops
from . import Fileview
from . import Img
from . import resize
from . import ICL
from . import FaceGrabber
from . import pprint_color
from . import Dlib_Face


class empty_class():
    pass

# class C():
#     def method(self, arg):
#         super().method(arg) 
# ccc= C()
# p2p = Pix2Pix_Train_Loop
# dir(p2p)

class Core:
    '''
    Examples:
        ###
        lm_file = ['shape_predictor_194_face_landmarks.zip','1fMOT_0f5clPbZXsphZyrGcLXkIhSDl3o']
        HelpCore.GdriveD.GdriveD(lm_file[1],lm_file[0])
        ###
        
    Main Functions:      
         ['BigHelp',
         'ColorPrint',
         'DelDig',
         'FaceGrabber',
         'FileView',
         'FlickrS',
         'GdriveD',
         'GlobX',
         'GooScrape',
         'HaarDetect',
         'ICrawL',
         'ImgCrawler',
         'ImgTools',
         'Logger',
         'MethHelp',
         'Ops',
         'Repo_List',
         'Resize',
         'ShowImg',
         'Sys_Cmd',
         'Sys_Exec',
         'Temp',
         'ZipUp']
         
    Sub functions:
         ['c_d',
         'cd',
         'cdr',
         'check_img_list',
         'cleanup_files',
         'cloner',
         'colab_root',
         'core_dirname',
         'core_filename',
         'core_pip_list',
         'cprint',
         'custom_pip_list',
         'custom_reps_setup',
         'docu',
         'explore_mod',
         'flickr_scrape',
         'gdrive_root',
         'getImagesWithID',
         'get_gdrive_dataset',
         'get_other_reps',
         'git_install_root',
         'haar_detect',
         'if_exists',
         'img_batch_rename',
         'importTboard',
         'install_repos',
         'into_func',
         'landmarkdetect',
         'landmarkdetecter',
         'landmarker',
         'list_to_file',
         'no_action',
         'path',
         'path_split',
         'rec_walk_folder',
         'rep',
         'root',
         'runProcess',
         'run_pip_installer',
         'set_maker',
         'sorted_repos',
         'sys_com',
         'sys_log',
         'system_log_file',
         'valid_img',
         'valid_list']
    '''
    def __init__(self):
        ''' set root paths '''
        print('[Setting paths]')
        self.root               = '/'                                                       # Absolute root
        self.colab_root         = self.root + 'content'                                     # Colab root        
        self.git_install_root   = self.colab_root + '/installed_repos'                      # Git install root
        self.gdrive_root        = self.colab_root+ '/drive/My Drive'                        # Google drive root
        self.core_dirname, self.core_filename = os.path.split(os.path.abspath(__file__))    # Core(self) dirname and filename
        
        ''' Inject functionality into the object '''
        print('[Running func injection]')
        self.BigHelp =      BigHelp
        self.Ops =          ops
        self.Repo_List =    RepCoList
        self.ColorPrint =   pprint_color.pprint_color
        self.GdriveD =      GdriveD
        self.FileView =     Fileview
        self.ZipUp =        ZipUp
        self.ImgCrawler =   GoImgScrape
        self.GooScrape =    gscrape
        self.Resize =       resize 
        self.Logger =       logger
        self.ImgTools =     Img.Tools
        self.ICrawL =       ICL.ICL
        self.DFace =        Dlib_Face
#         self.Pix2Pix =      Pix2Pix_Train_Loop
        
        ''' run pip, apt installers '''
        print('[Running pip installer]')
        self.run_pip_installer()
        
        ''' Setting some shortcuts '''
        print('[Shuffle Shit...]')
        ''' Facial landmark detector '''
        self.HaarDetect = self.haar_detect
        ''' Init a few modules '''
        self.ImgCrawler.GoogleImageCrawler()
        ''' Flickr scraper '''
        self.FlickrS = self.flickr_scrape
        ''' Show image '''
        self.ShowImg = self.ImgTools.ShowImg
        ''' Many repos in this list!!! '''
        self.sorted_repos = self.Repo_List.repos_sorted
        ''' Sys.exec en sys.log '''
        self.Sys_Exec = self.sys_com
        self.Logger.sys_log = self.sys_log
        ''' Better change dir '''
        self.c_d = self.cd       
        ''' Change to root folder '''
        self.c_d(self.root)
        ''' Existence checker '''
        self.if_exists = os.path.exists
        
        ''' cd  to root '''
        print('[Changing dir to root]')
        self.c_d(self.root)
        
        ''' In_helpers/helpers/ map '''
        print('[Installing repos]')
        inst_dir=self.core_dirname
        
        ''' cv2 and distro install '''
        cv_repos = [
#             'bxck75/opencv_contrib',
#             'bxck75/opencv', # long install
            'bxck75/face2face-demo',
            'bxck75/face-recognition',
        ]
        self.install_repos(cv_repos, inst_dir, False, True) 

        ''' needed googledrive repos '''
        gdrive_rps=[
            'bxck75/google-drive-list-shared', 
            'bxck75/PyDrive'
        ]
        self.install_repos(gdrive_rps, inst_dir, False, True)
    
        ''' pix2pix repos '''
        pix2pix_rps=[
                'bxck75/piss-ant-pix2pix',
        ]
        self.install_repos(pix2pix_rps, inst_dir,False,True)
        print('[Installing repos Done]')
        
        ''' PyDrive install '''
        print('[Installing PyDrive]')
        sr = self.Sys_Exec('python ' + self.git_install_root + '/PyDrive/setup.py install')
        import pydrive
        ''' google shared wrapper '''
        print('[Installing google wrapper]')
        sr += self.Sys_Exec('cp ' + self.git_install_root + '/google-drive-list-shared/google-drive-list-shared.py ' +  self.core_dirname + '/gdrive_shared.py')
        sr += self.Sys_Exec('rm -r ' + self.git_install_root + '/google-drive-list-shared')
        print(sr)

    def __repr__(self):
        return self.path
    
    '''###################################################################################################'''   
    '''                               sub methodes definitions bellow this line                           '''
    '''###################################################################################################'''
    
    def pix2pix(self, dataset_path, images_set_name, epochs=2, loops=2, mode='train', first_run=True, checkpoint=None):
        ''' 
        pix2pix Trainer/Predictor
            Definition :
                pix2pix(self, dataset_path, images_set_name, epochs=2, loops=2, mode='train', first_run=True)
            Example training:
                # new metrics 
                python pix2pix('/content/final_mages/train', 'faces', epochs=2, loops=2, mode='train', first_run=True)
                # default /content/metrics 
                python pix2pix('/content/final_mages/train', 'faces', epochs=2, loops=2, mode='train', first_run=False)
                # custom metrics 
                python pix2pix('/content/final_mages/train', 'faces', epochs=2, loops=2, mode='train', first_run=False, checkpoint='/content/metrics_abc')
            Example test:
                # default metrics forlder
                python pix2pix('/content/final_mages/train', 'faces', epochs=1, loops=1, mode='test', first_run=False)
                # custom metrics
                python pix2pix('/content/final_mages/train', 'faces', epochs=1, loops=1, mode='test', first_run=False, checkpoint='/content/metrics_abc')
        '''
        os.chdir(self.git_install_root + '/piss-ant-pix2pix')
        
        ''' set attributes '''
        self.dataset_path = dataset_path
        self.images_set_name = images_set_name
        self.epochs = str(epochs)
        self.mode = mode
        self.loops = loops
        self.first_run = first_run
        self.checkpoint = checkpoint
        
        ''' Set the checkpoint folder '''
        self.checkpoint_dir = self.root +'/' + self.images_set_name + '/metrics'
   
        ''' Run training '''
        def run_training(self, loops, checkpoint_dir, first_run, checkpoint):
            ''' Checkpoint payload '''
            for i in range(int(loops)):
                if first_run == False:
                    if checkpoint == None:
                        metrics = ' --checkpoint ' + checkpoint_dir
                        print('Metrics set to : ' + metrics)
                    else:
                        metrics = ' --checkpoint ' + checkpoint
                        print('Metrics set to : ' + metrics)
                else:
                    print("First loop! Creating the metrics from scratch!")
                    metrics = ''
                    
                ''' Train '''    
                r = self.sys_com('python pix2pix.py ' + metrics + ' \
                                                --input_dir ' + self.dataset_path + ' \
                                                --output_dir ' + self.checkpoint_dir + ' \
                                                --progress_freq 50 --mode self.mode  \
                                                --save_freq 100 --summary_freq 50 \
                                                --display_freq 50 --max_epochs '+ self.epochs + ' \
                                                --which_direction "BtoA"')
                
                ''' Loop ended check if first metrics have been saved '''
                if if_exists(self.GlobX(self.checkpoint_dir,'model-*.*')[0]):
                    self.first_run =  False
                    print('Model file exists. Setting first_run = ' + self.first_run)
                    ''' Clean up metrics and samples '''
                    self.cleanup_files(
                                    keep=9,
                                    cleanup_path=self.checkpoint_dir + '/images',
                                    search_pattern='*.*g',
                                    show_keepers=True
                                    )
                    self.cleanup_files(
                                    keep=9,
                                    cleanup_path=self.checkpoint_dir,
                                    search_pattern='model-*',
                                    show_keepers=False # only works on images
                                    )
                    self.cleanup_files(
                                    keep=9,
                                    cleanup_path=self.checkpoint_dir,
                                    search_pattern='event*',
                                    show_keepers=False # only works on images
                                    )
            return r
        
        run_training(self.loops, self.checkpoint_dir, self.first_run, self.checkpoint)
        os.chdir(self.root)

    def make_blank_img(self, w, h, black=True):
        ''' make empty image of w x h black or white '''
        ''' Example: '''
        '''  make_blank_img(self, w, h, black=True)  '''
        import numpy as np
        if black == True:
            # black blank image
            blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)   
        else:
            # white blank image
            blank_image = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
        return blank_image
    
    def lrange(self,lst):
        ''' range of length of list '''
        ''' Example: '''
        ''' lrange(lst) '''
        return range(len(lst)-1)
    
#     def combine_AB(self, dir_A, dir_B, out_dir='combine'):
#         ''' combine 2 image folders sidebyside'''
#         ''' Example: '''
#         ''' combine_AB(dir_A, dir_B, out_dir='combine') '''
        
#         import cv2
#         import matplotlib.pyplot as plt
#         import numpy as np

#         ''' get files in A '''
#         A_ptrn = 'landmark_blank_face_img_*.*g'
#         lst_A = self.GlobX( dir_A, A_ptrn)
#         lst_A.sort()
        
#         ''' get files in B '''
#         B_ptrn = 'face_img_*.*g'
#         lst_B = self.GlobX( dir_B, B_ptrn)
#         lst_B.sort()
        
#         ''' Combine the images sbs'''
#         for i in self.lrange(lst_A):
#             im1 = cv2.imread(lst_A[i])
#             im2 = cv2.imread(lst_B[i])
#             im_h = cv2.hconcat([im1, im2])
#             os.makedirs(self.root+'/'+out_dir, exist_ok=True)
#             ''' write new image '''
#             cv2.imwrite(self.root+'/'+out_dir+'/combined_img_%04d.jpg' % i, im_h)
            
#         ''' return list of new images '''
#         return self.GlobX(self.root+'/'+out_dir, '*.jpg')

    def resize_img(self, img_path, out_path,w=256,h=256):
        ''' resize_img(self, img_path, w=256,h=256) '''
        # log 
        log_msg = str([img_path, out_path,w,h])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        import scipy,cv2
#         img_path_arr = self.path_split(img_path)
        print(img_path)
#         print(img_path_arr)
        img = cv2.imread(img_path)
        ''' This will resize the image to size (width,height) '''
        resized_image = cv2.resize(img, (w,h))
        ''' Write image to out_dir '''
#         out_path = os.path.join(out_dir , img_path_arr['file'] + '.' + img_path_arr['ext'])
        print(out_path)
        cv2.imwrite(out_path, resized_image )
        return out_path
        

    def Face(self, img_in, num_points=68): # or num_points=194
        ''' Download and unzip the haar cascaders '''
        ''' Face(self, img_in, num_points=68) '''
        if num_points == 194:
            predictor_file_194 = ['shape_predictor_194_face_landmarks.zip','1fMOT_0f5clPbZXsphZyrGcLXkIhSDl3o']
            self.GdriveD.GdriveD(predictor_file_194[1],predictor_file_194[0])
            os.system('unzip ' + predictor_file_194[0])
            predictor_filename = os.path.join(self.git_install_root,predictor_file_194[0]).replace('zip','dat')
        else:
            predictor_file_68 = ['shape_predictor_68_face_landmarks.dat','1KNfN-ktxbPJMtmdiL-I1WW0IO1B_2EG2']
            self.GdriveD.GdriveD(predictor_file_68[1],predictor_file_68[0])
            predictor_filename = os.path.join(self.git_install_root,predictor_file_68[0])

        ''' Detector predictor loading'''
        import dlib
        print(predictor_filename)
#         detector = dlib.get_frontal_face_detector()
#         predictor = dlib.shape_predictor(predictor_filename)
        self.FaceAligner = self.DFace.AlignDlib(predictor_filename)
        R = self.FaceAligner.getAllFaceBoundingBoxes(img_in)
        print(R)
        plt.imshow(R)
        plt.show
    
    def num_files( self, folder ): 
        return len(self.GlobX(folder,'*'))

    def combine_pix2pix(self,fld1, fld2, target_folder):
        ''' combine 2 images of 2 folders and rename them sequencial'''
        # log 
        log_msg = str([fld1, fld2, target_folder])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        # Combine resized images with edge images side by side
        os.makedirs(target_folder, exist_ok = True)
        os.chdir('/content/installed_repos/piss-ant-pix2pix')
        self.sys_com('python tools/process.py --input_dir ' + fld1 + ' --b_dir ' + fld2 + ' --operation combine --output_dir ' + target_folder)
        print('combine')
        os.chdir(self.root)
        return self.num_files(target_folder)
    
    def combine_img_folders(self,fld1, fld2, target_folder, ptrn="*.*g"):
        ''' combine the images of 2 folders and rename them sequencial'''
        # log 
        log_msg = str([fld1, fld2, target_folder])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        fld1_img_paths = self.GlobX(fld1,ptrn)
        fld2_img_paths = self.GlobX(fld2,ptrn)
        target_list = fld1_img_paths + fld2_img_paths
        target_list.sort()

        # Combine resized images with edge images side by side
        os.makedirs(target_folder, exist_ok = True)
        for i in range(len(target_list)-1):
            print(target_list[i])
            target_new_name = target_folder + '/' + ('img_%04d.jpg' % i)
            print(target_new_name)
            self.sys_com('cp ' + target_list[i] + ' ' +  target_new_name )
        return len(target_list)
    
    
    def run_pip_installer(self,custom=False,custom_pip_list=None,merge=False):
        ''' 
            # Run core/custom pip installer
            # Define:
                run_pip_installer(self,custom=False,custom_pip_list=None,merge=False) 
            # Example:
                # Install core list
                self.run_installers()
            # Example:
                # Install custom list
                self.run_installers(custom=True,custom_list=['colorama', 'recognize_faces'])
            # Example:
                # Install merged custom/core list
                self.run_installers(custom=True,custom_list=['colorama', 'recognize_faces'], merge=True)
        '''
        self.custom_pip_list = custom_pip_list
        
        self.core_pip_list = [
            'colorama',
            'recognize_faces',
        ]
        if merge == True:
            ''' merge the core with the custom pip list'''
            self.merged_pip_list = self.custom_pip_list.update(self.core_pip_list)
            
        if custom == True:
            ''' install custom list '''
            if self.valid_list(self.custom_pip_list):
                ''' installed custom pip list '''
                for iter in range(len(self.custom_pip_list)-1):
                    print('[Installing]--> '+ self.custom_pip_list[iter])
                    os.system('pip install ' + self.custom_pip_list[iter])
                    print('[Done!]')
            return "[Custom list installed.]"

        else:
            ''' install core list '''
            if self.valid_list(self.core_pip_list):
                for iter in range(len(self.core_pip_list)-1):
                    print('[Installing]--> '+ self.core_pip_list[iter])
                    os.system('pip install ' + self.core_pip_list[iter])
                    print('[Done!]')
            return "[Core pip list installed.]"

    def get_file(self, file=None, adm=None):
        ''' 
        file to list method
        defaults to system.txt file 
            Example:
                Get_File(file='log.txt')            
        '''
        file_list = []
        # no system files without pwd
        if (file.split('.')[1] in ['sh','py','ipynb'] and adm != 'adm'):
            file = None
        if file == None:
            file = self.system_log_file
            
        with open(file,'r') as f:
            line = f.read()
            file_list.append(line)
        return file_list
    import sys
    
    import os
    import dlib
    import glob
    import cv2
    import numpy as np
    import dlib
    import matplotlib.pyplot as plt

    def FaceRip(self,folder='/content/final_loot', num_points=68):
        ''' 
            Rip all faces from a images folder
            Example:
                FaceRip(folder='/content/portrait')
        '''
        ''' Download and unzip the haar cascaders '''
        # log 
        log_msg = str([folder, num_points])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        predictor_file_194 = ['shape_predictor_194_face_landmarks.zip','1fMOT_0f5clPbZXsphZyrGcLXkIhSDl3o']
        predictor_file_68 = ['shape_predictor_68_face_landmarks.dat','1KNfN-ktxbPJMtmdiL-I1WW0IO1B_2EG2']
        if num_points == 194:
            self.GdriveD.GdriveD(predictor_file_194[1],predictor_file_194[0])
            os.system('unzip ' + predictor_file_194[0])
            predictor_filename = os.path.join(self.git_install_root,predictor_file_194[0]).replace('zip','dat')
        else:            
            self.GdriveD.GdriveD(predictor_file_68[1],predictor_file_68[0])
            predictor_filename = os.path.join(self.git_install_root,predictor_file_68[0])
            
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(predictor_filename)

        ''' glob the folder '''
        lst = self.GlobX(folder,'*.*g')

        ''' iterate of the images and save the faves and landmarks'''
        for im in self.lrange(lst):
            # load the image
            img = cv2.imread(lst[im])
            org_shape_w, org_shape_h, org_shape_c = img.shape
            
            # make black empty ghost image of size res2
            layer1 = np.zeros((org_shape_w, org_shape_h, 4))
            transpblank =  layer1[:]   
            orgblank  = self.make_blank_img( org_shape_w, org_shape_h, black=True)
 
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

                size_increase = 50 # increase size of face image output

                # cut out face without landmarkers
                res2 = img[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
                gray2 = gray[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]

                # make dirs
                os.makedirs(self.root+'/faces/not_marked', exist_ok=True)
                
                # save face withoutmarkers
                cv2.imwrite(self.root+'/faces/not_marked/face_img_'+str(im)+'.jpg', res2)
                cv2.imwrite(self.root+'/faces/not_marked/face_img_'+str(im)+'.jpg', res2)

                # get the landmarks of the face
                landmarks = predictor(gray, face)
                for n in range(0, num_points):
                    x = landmarks.part(n).x
                    y = landmarks.part(n).y
                    # draw landmarks on all backgrounds
                    cv2.circle(img, (x, y), 4, (255, 0, 100), -1)
                    cv2.circle(gray, (x, y), 4, (255, 100, 0), -1)
                    cv2.circle(orgblank, (x, y), 4, (255, 100, 0), -1)
                    cv2.circle(transpblank, (x, y), 4, (255, 100, 0), -1)
                
                # face images
                org_with_marks = img[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
                gray_with_marks = gray[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
                blank_with_marks = orgblank[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]
                transp_with_marks = transpblank[y1-size_increase :y2+size_increase ,x1-size_increase :x2+size_increase ]

                #save face images
#                 os.makedirs(self.root+'/faces/org', exist_ok=True)
#                 os.makedirs(self.root+'/faces/gray', exist_ok=True)
#                 os.makedirs(self.root+'/faces/blank', exist_ok=True)
                os.makedirs(self.root+'/faces/transp', exist_ok=True)
                
#                 cv2.imwrite(self.root+'/faces/org/face_img_'+str(im)+'.jpg', org_with_marks)
#                 cv2.imwrite(self.root+'/faces/gray/face_img_'+str(im)+'.jpg', gray_with_marks)
#                 cv2.imwrite(self.root+'/faces/blank/face_img_'+str(im)+'.jpg', blank_with_marks)
                cv2.imwrite(self.root+'/faces/transp_marks/face_img_'+str(im)+'.jpg', transp_with_marks)

            # save total  
            os.makedirs(self.root + '/proc_images/total/img_org', exist_ok=True)
            os.makedirs(self.root + '/proc_images/total/img_gray', exist_ok=True)
            os.makedirs(self.root + '/proc_images/total/img_blank', exist_ok=True)
            os.makedirs(self.root + '/proc_images/total/img_transp', exist_ok=True)
            
            cv2.imwrite(self.root + '/proc_images/total/img_org/landmarked_'+str(im)+'.jpg', img)
            cv2.imwrite(self.root + '/proc_images/total/img_gray/landmarked_'+str(im)+'.jpg', gray)
            cv2.imwrite(self.root + '/proc_images/total/img_blank/landmarked_'+str(im)+'.jpg', orgblank)
            cv2.imwrite(self.root + '/proc_images/total/img_transp/landmarked_'+str(im)+'.jpg', transpblank)
            
        ''' get list of saved face images '''
        folder_A = self.root+'/faces/not_marked'
        folder_B = self.root+'/faces/transp'
        
        org_faces_lst = self.GlobX(folder_A, '*.jpg')
        landmarks_lst = self.GlobX(folder_B, '*.jpg')
        

        ''' resize all of them'''
        os.makedirs(folder_A, exist_ok=True)
        for i in self.lrange(org_faces_lst):
            if self.valid_img(org_faces_lst[i],'jpg'):
                print(org_faces_lst[i]+'--->',end='')
                print(org_faces_lst[i].replace('/faces','/resized_faces'))
                try:
                    self.resize_img(org_faces_lst[i], org_faces_lst[i].replace('/faces','/resized_faces'),256,256)
                except:
                    print([org_faces_lst[i], org_faces_lst[i].replace('/faces','/resized_faces'),256,256])
                    pass                        
            
        os.makedirs(folder_B, exist_ok=True)
        for i in self.lrange(landmarks_lst):
            if self.valid_img(landmarks_lst[i],'jpg'):
                print(landmarks_lst[i]+'--->',end='')
                print(landmarks_lst[i].replace('/faces','/resized_faces'))
                try:
                    self.resize_img(landmarks_lst[i], landmarks_lst[i].replace('/faces','/resized_faces'),256,256)
                except:
                    print(landmarks_lst[i], landmarks_lst[i].replace('/faces','/resized_faces'),256,256)
                    pass
            
        ''' return resized files list '''    
        return self.GlobX(self.root + '/resized_faces', '*.jpg')[:].sort()
        
        
    def haar_detect(self, in_img, out_img):
        ''' detect faces'''
        '''
            Detect faces and landmarks
                Example:
                    haar_detect( img_in, img_out)
        '''
        import cv2 as cv
        import matplotlib.pyplot as plt
        import sys
        img = cv.imread(in_img)
        cascade_fn = "/content/installed_repos/Python_Helpers/Helpers/haarcascade_frontalface_alt.xml"
        nested_fn  = "/content/installed_repos/Python_Helpers/Helpers/haarcascade_eye.xml"
        cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))
        nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))
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
        plt.imshow('facedetect', vis)
        cv.imwrite(out_img,vis)
        return out_img 

    
    def getImagesWithID(img_folder):
        ''' images with ids '''
        import os
        import cv2
        import numpy as np 
        from PIL import Image
        
        def run_recognizer(path):
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            if not os.path.exists('/content/recognizer'):
                os.makedirs('/content/recognizer')
            imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
            faces = []
            IDs = []

            for imagePath in imagePaths:
                faceImg = Image.open(imagePath).convert('L')
                faceNp = np.array(faceImg,'uint8')
                ID = int(os.path.split(imagePath)[-1].split('.')[1])
                faces.append(faceNp)
                IDs.append(ID)
                # plt.imshow("training",faceNp)
                cv2.waitKey(10)
            return np.array(IDs), faces     
        Ids, faces = run_recognizer(img_folder)
        recognizer.train(faces,Ids)
        recognizer.save('/content/recognizer/trainingData.yml')
        cv2.imwrite(out_img,vis)
        cv2.destroyAllWindows()
        
    def Temp(self, img ):
        import cv2
        import numpy as np 
        import sqlite3
        import os
        conn = sqlite3.connect('database.db')
        if not os.path.exists('./dataset'):
            os.makedirs('./dataset')
        c = conn.cursor()
        face_cascade = cv2.CascadeClassifier('/content/installed_repos/Python_Helpers/Helpers/haarcascade_frontalface_alt.xml')
        cap = cv2.VideoCapture(0)
        uname = input("Enter your name: ")
        c.execute('INSERT INTO users (name) VALUES (?)', (uname,))
        uid = c.lastrowid
        sampleNum = 0
        while True:
          ret, img = cap.read()
          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          faces = face_cascade.detectMultiScale(gray, 1.3, 5)
          for (x,y,w,h) in faces:
            sampleNum = sampleNum+1
            cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.waitKey(100)
#           cv2.imshow('img',img)
          cv2.waitKey(1);
          if sampleNum > 20:
            break
        cap.release()
        conn.commit()
        conn.close()
        cv2.destroyAllWindows()   
        
    
    def path_split(self, full_path):
        ''' split s path into a dict '''
        ''' path_split(full_path) '''
        r = {}
        r['full_path'] = full_path
        drive, path_and_file = os.path.splitdrive(full_path)
        path, file = os.path.split(path_and_file)
        file_name, ext = file.split('.')
        r.update({'path': path.split('/')[1:],'file' : file_name, 'ext' : ext})
        return r

    def DelDig(self, list): 
        '''
            # Driver code  
            # https://gist.githubusercontent.com/bxck75/dc0ef99833af8a2b2533c2d1634d24d0/raw/212feb5df1f89e1f2bce1e8b3c0c10015f875e93/DelDig.py
            list = ['4geeks', '3for', '4geeks'] 
            print(DelDig(list))
        '''
        import re 
        pattern = '[0-9]'
        list = [re.sub(pattern, '', i) for i in list] 
        return list

    
    def cloner(self, img_path):
        ''' 
            clone the originals and return tuple of org and marked path
            cloner('/content/images/img_1.jpg',204) 
        '''
        ILIST = self.GlobX(img_path, '*.*g')
        for im in range(0, len(ILIST)):
            drive, path_and_file = os.path.splitdrive(ILIST[im])
            path, file = os.path.split(path_and_file)
            file_name, ext = file.split('.')
            ''' strip old numbers from filename '''
            print(self.DelDig(ILIST))
            ''' compose the new paths '''
            org_path = path + '/org/' + file_name + '_%4d.%s' %  im, ext
            marked_path = path + '/marked/' + file_name + '_%4d.%s' %  im, ext
            ''' copy directly from inputfolder to org folder as working copy '''
            copy_to_org_cmd = os.path.join( path, file ) + ' ' + org_path
            os.system('cp ' + copy_cmd )
            ''' 
                Send img to the landmarker 
                with marked folder as return path 
            '''
            if mode == 'landmarker':
                ''' landmark processes for pix2pix dataset '''
                self.landmarker(org_path , marked_path)
            elif mode == 'haar':
                ''' other processes to make set '''
                self.haar_detect(org_path , marked_path)
            elif mode == 'colorizer':
                ''' other processes to make set '''
            elif mode == 'edged':
                ''' other processes to make set '''
            else:
                print('No mode picked!...')
                sys.exit(1)
            ''' counter 1 up '''
            ti += 1
            '''   End of loop   '''
    
    def landmarker(self, input_path, output_path):
        ''' 
            landmark image the originals and return tuple of org and marked path
            landmarker(self, input_path, output_path):
            Example:
            landmarker('/content/images/org/img_1.jpg','/content/images/marked/img_1.jpg') 
        '''
#         print(__doc__)
        '''landmark the image'''
        img = cv2.imread(input_path)
        if img is None:
            print('Failed to load image file:', input_path)
            sys.exit(1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lsd = cv2.line_descriptor_LSDDetector.createLSDDetector()
        lines = lsd.detect(gray, 1, 1)
        for kl in lines:
            if kl.octave == 0:
                # cv.line only accepts integer coordinate
                pt1 = (int(kl.startPointX), int(kl.startPointY))
                pt2 = (int(kl.endPointX), int(kl.endPointY))
                cv2.line(img, pt1, pt2, [255, 0, 0], 2)           
        print(output_path)
        cv2.imwrite(output_path, img)
        
        
        
    def install_repos(self, repos, inst_dir, sub_repos=False, chadir=False):
        '''
        Example:
            inst_dir='/content/images'
            repos=['bxck75/piss_ant_pix2pix','bxck75/opencv']
            install_repos(repos, inst_dir)
        '''
        # log 
        log_msg = str([repos, inst_dir, sub_repos, chadir])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        self.sys_com('mkdir -p '+self.git_install_root)
#         print(self.git_install_root)
        for rep in repos:
            self.rep=rep.split('/')
            # change folder check
            if chadir == True:
                #Switch to path
                os.chdir(self.git_install_root)
                # pull the git repo
                self.sys_com('git clone https://github.com/'+self.rep[0]+'/'+self.rep[1]+'.git')
                # Set the return value for rep rootpath
                self.path=self.git_install_root+'/'+self.rep[1]
            # show imported files
            self.sys_com('ls ' + inst_dir)
        # run custom setups and get other reps
#         self.custom_reps_setup()
        if sub_repos == True:
            self.get_other_reps()
        

    def cprint(self, msg, style='info'):
        ''' set color output '''
        dir(ColorPrint)
#         mod, meth, func = 'ColorPrint','ColorPrint','print_'+style
#         c_p_f = __import__(mod+'.'+meth+'.'+func, globals(), locals(), ['msg', 'style'], -1)
#         print(c_p_f.__name__)
#         self.msg = c_p_f.msg
#         self.style= c_p_f.style
# #         
#         cprint_func = self.into_func(mod, meth, func)
#         cprint_func(msg)
#         self.print_fail = ColorPrint.ColorPrint.print_fail
#         self.print_pass = ColorPrint.ColorPrint.print_pass
#         self.print_warn = ColorPrint.ColorPrint.print_warn
#         self.print_info = ColorPrint.ColorPrint.print_info
#         self.print_bold = ColorPrint.ColorPrint.print_bold
    def rainbow(self):
        ''' print a rainbow '''
        help(self.ColorPrint)
        
        
    def GlobX(self, path_in, pattern_in):
        ''' Glob folders on pattern '''
        # log 
        log_msg = str([path_in, pattern_in])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        import os
        os.system('sudo pip install pywildcard')
        import pywildcard as fnmatch
        treeroot=path_in
        pattern=pattern_in
        Sheisterhaufen = []
        for base, dirs, files in os.walk(treeroot):
            goodfiles = fnmatch.filter(files, pattern)
            Sheisterhaufen.extend(os.path.join(base, f) for f in goodfiles)
        print(Sheisterhaufen)
        return Sheisterhaufen
    

    def flickr_scrape(self,query= ['portrait'],qty=5,dest='/content/images'):
        '''
            Example:
                search_list,img_dir,qty = ['portait','face'], 'images', 21
                flickr_scrape(search_list,qty,img_dir)
        '''
        # log 
        log_msg = str([query,qty,dest])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg ) 
        print("Running queries:"+str(query)+' qty:'+str(qty)+' dest:'+dest)
        if (len(query) > 0 and str(qty) != '' and dest != '' ):
            ''' Let the scapers scrape! '''
            os.system('sudo pip install gallery-dl')
            if isinstance(query, list):
                for s in query:
                    keyword=s.replace(' ', '+')
                    self.sys_com('gallery-dl --range 1-' + str(qty) + ' -d ' + dest + ' https://flickr.com/search/?text='+keyword)
            else: 
                keyword=str(query.replace(' ', '+'))
                self.sys_com('gallery-dl --range 1-' + str(qty) + ' -d ' + dest + ' https://flickr.com/search/?text='+keyword)

        ''' see if they are downloaded '''
        img_list = self.GlobX(str(dest),'*.jpg')
        print(len(img_list))
        i=0 # iterator for filename
        for img in img_list:
            print(img)
#             self.sys_com('cp '+img+' '+str(self.root_dirname)+'/images/img_%d.jpg'%(i+1))
            self.sys_com('cp '+img+' '+str(dest)+'/img_%d.jpg'%(i+1))      
            i+=1 # up iterator
        print(str(i)+' images copied!')
        ''' Remove flickr folder when images are moved and renamed'''
        self.sys_com('rm -r '+str(dest)+'/flickr')

        
    def if_exists(self, path):
        ''' check if path leads somewhere '''
        func_name=inspect.stack()[0][3]
        try:
            if os.path.exists(path):
                log_msg =  path + ' File exists! '
                self.sys_log(func_name + ' <~[LOGGED]~> ' + log_msg)
                return True
            else:
                log_msg =  path + ' File Does not exists! '
                self.sys_log(func_name + ' <~[LOGGED]~> ' + log_msg ) 
                return False
        except:
            log_msg =  path + ' Error while checking file! '
            self.sys_log(func_name + ' <~[LOGGED]~> ' + log_msg )
            return False
            
    def list_to_file(self, list_to_write, file_name):
        ''' list of items into a txt file '''
        # log 
        log_msg =  'List ' + str(list_to_write) + ' to file ' + file_name 
        func_name=inspect.stack()[0][3]
        self.sys_log(func_name + ' <~[LOGGED]~> ' + log_msg)
        for line in list_to_write:
            self.sys_log(line,  file_name)
        
    def sys_log(self, msg, log_name='system'):
        '''
        Example:
            log_msg = "Empty command string. did you first set the CMD arg?"
            self.sys_log(str([ self.insp(), ' <~[LOGGED]~> ', log_msg ]))
        '''
        self.system_log_file = self.colab_root + '/' + log_name + '.txt'
        if self.if_exists(self.system_log_file):
            fh = open(self.system_log_file, 'a+' )
            fh.write(str(msg)+'\n')
            fh.close()
        else:
            fh = open(self.system_log_file, 'w' )
            fh.write(str(log_name +'logfile')+'\n')
            fh.close()
                   
    def runProcess(self):
        ''' 
            run subprocess from self.CMD
        '''
        import subprocess
#         log_msg = str(self.Sys_Cmd)
#         func_name=inspect.stack()[0][3]
#         self.sys_log(func_name + '<~[LOGGED]~>' + log_msg )                          
        # check if is valid command string
        if ( self.Sys_Cmd != None and len( self.Sys_Cmd ) > 0 ):
            # run the subprocess
            sproc = subprocess.Popen(self.Sys_Cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            # log 
            log_msg = "Empty command string. did you first set the CMD arg?"
            self.sys_log(str([self.insp(), ' <~[LOGGED]~> ', log_msg]))
            return log_msg
        while(True):
            # returns None while subprocess is running and 0 when finished
            retcode = sproc.poll()
            # meanwhile it outputs lines of the pipe
            line = sproc.stdout.readline()
            # if line not is None yield line
            if line is not None:
                yield line
            # if retcode not is None break
            if retcode is not None:
                break

    def sys_com(self,cmd):
        ''' 
            Execute system command and get output 
            cmd = 'ls'
            sys_com(cmd)
        '''  
        log_msg = cmd
        func_name=inspect.stack()[0][3]
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg)
        results = []
        #  for lines in output of the subprocess
        self.Sys_Cmd = cmd.split(' ')
        for line in self.runProcess():
            # if decoded line is not empty
            if line.decode('utf-8') != '':
                # append the line to results list
                results.append(line.decode('utf-8').replace("\n",''))
        # return results    
        return results
            
    def rec_walk_folder(self, folder, output='files'):
        ''' 
            recursive print contents of folder 
                rec_walk_folder(folder)
        '''
        result_files = []
        result_folders = []
        # list all recursive
        for root, folders, files in os.walk(folder, topdown=False):
            # files 
            for file_name in files:
#                 print(os.path.join(root, file_name))
                result_files.append(os.path.join(root, file_name))
            # folders
            for folder_name in folders:
#                 print(os.path.join(root, folder_name))
                result_folders.append(os.path.join(root, folder_name))            
        # return resulting files and folders lists
        return result_files, result_folders
    
    
    def cd(self,dir,show=False):
        ''' 
            change dir and show 
                cd(dir,show=True) 
        '''
        os.chdir(dir)
        if show == False:
            return dir
        else:       
            return self.rec_walk_folder(dir)

        
    def cdr(self,ls=False, root='/content'):
        ''' 
            change dir to root [ or other ] 
                cdr(ls=True, root='/content')
        '''
        return cd(root,ls)

    
    def valid_img(self, filename, type_img='png'):
        '''
            validate jpg or png files
                valid_img(filename, type_img='png')
        '''
        from PIL import Image
        log_msg = str(filename)
        func_name=inspect.stack()[0][3]
        self.sys_log(func_name + '<~[LOGGED]~>' + log_msg )      
        try:
            i=Image.open(filename)
            if type_img == 'jpg':
                if i.format =='JPEG':
                    return True
            elif type_img == 'png':
                if i.format =='PNG':
                    return True
            else:
              print('deleting '+ i.format)
              os.remove(filename)
              return False
    
        except IOError:
            print('deleting '+ filename)
            os.remove(filename)
            return False

        
    def valid_list(self, lst):
        '''
            validate list if not empty
            valid_list(self, lst)
        '''
        log_msg = str(lst)
        func_name = inspect.stack()[0][3]
        self.sys_log(func_name + '<~[LOGGED]~>' + log_msg ) 
        if len(lst) > 0:
            return True
        else:
            return False

        
    def check_img_list(self, img_list, ext='png'):
        '''
            check images list and remove bad files 
                check_img_list((img_list, ext='png')
        '''
        log_msg = str([img_lst, ext])
        func_name = inspect.stack()[0][3]
        self.sys_log(func_name + '<~[LOGGED]~>' + log_msg ) 
        img_list = sorted(img_list)
        print('checking images list')
        if self.valid_list(img_list):
            for f in img_list:
                if not self.valid_img(f,ext):
                    os.remove(f)      
     
    def cleanup_files(self, keep, cleanup_path, search_pattern='*.*g', show_keepers=False):
        '''
            Example:
                cleanup_files(
                            keep=16,
                            cleanup_path='/content/test',
                            search_pattern='*.*g',
                            show_keepers=True
                            )        
            show_keepers only works with images else will crash the process
        '''
        # log 
        log_msg = str([keep, cleanup_path, search_pattern, show_keepers])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg )    
        import dlib
        import matplotlib.pyplot as plt
        # clean up images
        img_list = self.H.Me(['globx', cleanup_path, search_pattern])
        img_list.sort(key=lambda f: os.path.getmtime(os.path.join(cleanup_path, f)))
#         img_list = sorted(img_list)
        print(img_list)
        if len(img_list) > keep:
            if show_keepers == True:  
                # keepers list  
                latest = img_list[-keep:]    
                # show the keepers list
                for i in range(keep):
                    print("Keeping " + latest[i] )
                    img = dlib.load_rgb_image(latest[i]) 
                    plt.imshow(img)
                    plt.show()
            # delete keepers from the image list
            del img_list[-keep:]
            # delete files left in the image list
            for i_file in img_list:
                print('deleting : ' + i_file)
                os.remove(i_file)

    
    def into_func(self,mod,meth,func=None):
        ''' 
        load a module.meth.func from string
            Example 1:
                mod='IPython'
                meth='display'
                into_func(mod, meth) 
            Example 2:
                mod='IPython'
                meth='display'
                func='clear_output'
                into_func(mod, meth, func)
        '''
        # log 
        log_msg = str([mod,meth,func])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg )
        
        import importlib
        module=mod
        method=meth
        if func == None:
            print(module + '.' + method+' <-- Is now a function from string')
            function_string = module + '.' + method  # 'IPython.display.Audio'
        else:
            function=func
            print(module + '.' + method+'.' + function+' <-- Is now a function from string')
            function_string = module + '.' + method + '.' + function  # 'IPython.display.Audio'
        ''' split the string '''
        mod_name, func_name = function_string.rsplit('.',1)
        ''' load module '''
        mod = importlib.import_module(mod_name)
        ''' return the attributes of the modules function '''
        return getattr(mod, func_name)
    
    
    def explore_mod(self, mod, meth, only_root_mod=False):
        ''' Explore modules and methods '''
        from pprint import pprint as prpr
        func = self.into_func(mod, meth)
        if only_root_mod==False:
            results_list = []
            vdir_result = self.H.Me([ 'vdir',func])            
            ''' ADD RESULTS OF THE MAIN MODULES '''
            results_list.append([mod, vdir_result])
            for i in range(len(vdir_result)-1):
                submod_func = self.into_func(mod, meth, vdir_result[i])                
                ''' Help for functions and classes '''
                if (str(submod_func).split(' ')[0] == '<function' or str(submod_func).split(' ')[0]  == '<class'):
                    # Function exploration logic
                    self.cprint('#' * 50, style='warn')
                    print('--- ' + str(submod_func) + ' ---', end='')
                    self.cprint('#' * 50, style='fail')
                ''' ADD RESULTS OF THE SUB MODULES '''
                results_list.append([submod_func, self.H.Me( [ 'vdir', self.into_func(mod, meth, vdir_result[i]) ] )]) 
            ''' return as a list '''
            return results_list
        ''' return root as list '''
        return [mod, self.H.Me([ 'vdir', func])]

    
    def docu(self, mo = 'Helpers',me = 'core'):
        '''
        Get recursive help on modules
        Usage :
            docu(mo = 'Helpers',me = 'core')
        '''
        from pprint import pprint as prpr
        import importlib
        mod = importlib.import_module(mo)
        prpr(self.H.Me(['vdir',mod]))
        res = self.explore_mod(mo, me)
        prpr(res)
        
    
    def img_batch_rename(self,directory_in,directory_out,file_prefix):    
        '''
            Usage:
                folder_to_rename= '/content/images'
                folder_renamed_files = 'content/img_renamed'
                file_name_prefix = "img"
                img_batch_rename(folder_to_rename,folder_renamed_files,file_name_prefix)
        '''
        from PIL import Image
        import os,sys,glob
        # directory=sys.argv[1]
        i=int(0)
        for infilename in glob.iglob(directory_in+'/*.*g'):
            im = Image.open(infilename)
            rgb_im = im.convert('RGB')
            outfilename = "/"+file_prefix+"_%d.png" % int(i + 1)
            outfile=os.path.join(directory_out, outfilename)
            print(directory_out+outfile)
            rgb_im.save(directory_out+outfile)
            i += 1
        
    def get_gdrive_dataset(self,pack='pail', DS_root='datasets',GD_root='datasets'):
        import google
        from google.colab import drive
        drive.mount('/content/drive', force_remount=True)
        self.H.GD_ROOT='/'+GD_root+'/'
        self.H.DS_ROOT='/'+DS_root+'/'
        os.chdir(self.Gdrive_root+self.H.GD_ROOT)
        self.H.Me(['mkd',[DS_root,'models'],self.root_dirname])
        self.sys_com('cp -r '+pack+' '+self.root_dirname+self.H.DS_ROOT)
        os.chdir(self.root_dirname+self.H.DS_ROOT)
        self.sys_com('unzip -q '+pack)
        self.sys_com('rm -r '+pack)
        os.chdir(self.root_dirname)

    def MethHelp(self,libs):
        os_help=self.HelpCore.explore_mod(libs)
        #make a list containing libs values of os_help
        listOfLibs = [x[0] for x in os_help]
        #make a list containing libs method values of os_help
        listOfMethods= [x[1] for x in os_help]
        # Create a zipped list of tuples from above lists
        zippedList =  list(zip(listOfLibs, listOfMethods[0:5]))
        zippedList
        # request help on method from list
        return zippedList

    def importTboard():
        '''load tensorboard'''
        import datetime, os ,tensorboard 
        
#     def load_helpers(self):
#         '''load BigHelp to gdrive obj'''
# #         self.C = BigHelp
# #         return BigHelp.Helpers()

#     def load_zipper(self):
#         '''load zipup to gdrive obj'''
# #         self.C = BigHelp
# #         return ZipUp.ZipUp

    def set_maker(_in_,_mode_,_out_):
        '''
           set_maker(_in_,_mode_,_out_):
        '''
        #     global r
        self.sys_com('python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(self.root_dirname)+'/images_resized')
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(M.root_dirname)+'/images_resized')
        self.sys_com('echo python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(self.root_dirname)+'/images_resized --operation blank --output_dir '+str(self.root_dirname)+'/images_blank')
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation blank --output_dir '+str(M.root_dirname)+'/images_blank')
        self.sys_com('echo python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(self.root_dirname)+'/images_resized --operation edge --output_dir '+str(self.root_dirname)+'/images_edge')
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation edge --output_dir '+str(M.root_dirname)+'/images_edge')
        if _mode_ != '':
            self.sys_com('echo python ' + str(self.root_dirname)+'/tools/process.py --input_dir ' + str(self.root_dirname)+'/images_' + _mode_ +' --operation combine --output_dir ' + str(_out_))
        #         os.system('echo python ' + str(M.root_dirname)+'/tools/process.py \
        #             --input_dir ' + str(M.root_dirname)+'/images_' + _mode_ + ' \
        #             --operation combine \
        #             --output_dir ' + str(_out_))

        
        

# #     old method router
#     def Me(self, args):
#         """Dispatch method"""
#         # glob the args
#         self.root_path='/content/'
# #         print(self.root_path)
#         self.args = args
#         print('[Running-->]'+str(self.args))
#         self.method= self.args[0]
#         self.method_args= self.args[1:]
#         method_args = self.method_args
#         method_name = '_' + str(self.method)
#         # Get the method from 'self'. Default to a lambda.
#         method = getattr(self, method_name, lambda: self.no_action())
#         # Call the method as its returned
#         return method()

    # HELPER FUNCTIONS
    # facial landmarks
    def landmarkdetecter(self,img):
        self.Me(['pip',['face_recognition']])
        from PIL import Image
        import face_recognition

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(img)

        # Find all the faces in the image using the default HOG-based model.
        # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
        # See also: find_faces_in_picture_cnn.py
        face_locations = face_recognition.face_locations(image)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
        pil_image.show()
        
        
        
    #facial landmarks
    def landmarkdetect(self,img):
        self.Me(['pip',['face_recognition']])
        from PIL import Image, ImageDraw
        import face_recognition

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(img)# /home/rishika/Pictures/multi1.jpg

        # Find all facial features in all the faces in the image
        face_landmarks_list = face_recognition.face_landmarks(image)

        print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

        # Create a PIL imagedraw object so we can draw on the picture
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for face_landmarks in face_landmarks_list:

            # Print the location of each facial feature in this image
            for facial_feature in face_landmarks.keys():
                print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

            # Let's trace out each facial feature in the image with a line!
            for facial_feature in face_landmarks.keys():
                d.line(face_landmarks[facial_feature], width=5)
        # Show the picture
        pil_image.show()

        #comment

    # method Args discloser
    def _get_args(self):
        from inspect import signature
        print(signature(self.method_args[0]))
#         print(self.method_args)
#         self.args_target=self.method_args[0]
#         print(inspect.isasyncgenfunction(self.args_target))

    # print methods of an object
    def _methods_of(self,lr=False):
        for attr in dir(self.method_args[0]):
            if attr.startswith("_"): continue
            try:
                if callable(getattr(self.method_args[0],str(attr),None)):
                    print(f"{attr}{str(inspect.signature(getattr(self.method_args[0],str(attr), None)))}:")
                    if lr==True: print()
            except: pass

    # Folder globber
#     def _globx(self):
#         import os
#         os.system('sudo pip install pywildcard')
#         import pywildcard as fnmatch
# #         print(self.args)
#         treeroot=self.method_args[0]
#         pattern=self.method_args[1]
#         Sheisterhaufen = []
#         for base, dirs, files in os.walk(treeroot):
#             goodfiles = fnmatch.filter(files, pattern)
#             Sheisterhaufen.extend(os.path.join(base, f) for f in goodfiles)
#         return Sheisterhaufen

#     # CMD-LINE subprocess spawner
#     def _cml(self): 
#         Sheisterhaufen =[]
#         cmd=self.method_args[0]
#         if len(self.method_args) > 1:
#             fi=self.method_args[1]
#         else: # only False needs to be fed
#             fi=True
#         nepopso = os.popen(cmd)
#         try: # Yeah try that u popo!!!
#             for line in nepopso:
# #                 line.encode("utf-8") Mightbe on older python
#                 if fi == True:
#                     Sheisterhaufen.append(line.replace('\n',''))
#         finally: # yeah finally done pooping!!!!!
#             nepopso.close()
#         return Sheisterhaufen
    
    # Flickr scraper
    # TODO: make this the main gallery-dl wrapper class and include it 
    # I can then us the API to it full sambal power and scrape 200+ galleries!!!

    # Method discloser
    def _vdir(self):
        if len(self.method_args)==0:
            return [x for x in dir(self) if not x.startswith('__')]
        else:
            if isinstance(self.method_args[0], list):
                elem=[]
                for m in self.method_args[0]:
                    elem.append([m.__name__,[x for x in dir(m) if not x.startswith('__')]])
                return elem 
            else:   
                return [x for x in dir(self.method_args[0]) if not x.startswith('__')]
    
    # Pip installer
    def _pip(self):
        import os
        print()
        self.pip_install_list = self.method_args[0]
        if isinstance(self.pip_install_list, list):
            spaced_list=''
            for s in self.pip_install_list:
                spaced_list += str( s + ' ' )
            # install the space separated list
            print('Installing ' + spaced_list)
            self.sys_com('pip install ' + spaced_list)
        else: 
            # install the single pip lib
            print('Installing ' + self.pip_install_list)
            self.sys_com('pip install ' + self.pip_install_list)
            
    # Folder spawner
    def _mkd(self):
        import os
        if isinstance(self.method_args[0], list):
            for x in self.method_args[0]:
                os.makedirs(self.method_args[1] + '/' + str(x), exist_ok = True)
        else:
            os.makedirs(self.method_args[1]+'/'+self.method_args[0], exist_ok = True)
            
#     # Pull all selected reps  
#     def _inst_reps(self):
#         self.repo_list=self.method_args[0]      
#         self.git_install_root=self.method_args[1]
#         self.sub_repos=self.method_args[2]
#         self.chadir=self.method_args[3]
#         self.sys_com('mkdir -p '+self.git_install_root)
# #         print(self.git_install_root)
#         for rep in self.repo_list:
#             self.rep=rep.split('/')
#             # change folder check
#             if self.chadir == True:
#                 #Switch to path
#                 os.chdir(self.git_install_root)
#                 # pull the git repo
#                 self.sys_com('git clone https://github.com/'+self.rep[0]+'/'+self.rep[1]+'.git')
#                 # Set the return value for rep rootpath
#                 self.path=self.git_install_root+'/'+self.rep[1]
#         # show imported files
#         self.sys_com('ls ' +self.path)
#         # run custom setups and get other reps
# #         self.custom_reps_setup()
# #         if self.sub_repos == True:
# #             self.get_other_reps()
        
    # get GPU Capabilities    
    def _get_gpu(self):
    #     check gpu
        import tensorflow as tf
        tf.test.gpu_device_name()
        self.sys_com('ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi')
        self.sys_com('pip install gputil')
        self.sys_com('pip install psutil')
        self.sys_com('pip install humanize')
        import psutil
        import humanize
        import os
        import GPUtil as GPU
        GPUs = GPU.getGPUs()
        # XXX: only one GPU on Colab and isn’t guaranteed
        gpu = GPUs[0]
        def printm():
         process = psutil.Process(os.getpid())
         print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " I Proc size: " + humanize.naturalsize( process.memory_info().rss))
         print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
        printm()

    #--repository required dependancies setup
    def custom_reps_setup(self):
        # custom stuff for CartoonGAN-tensorflow and keras-team/keras-contrib
        if 'keras-team/keras-contrib' in self.repo_list:
            os.chdir(self.path+'/keras-contrib')
            self.sys_com('python convert_to_tf_keras.py')
            self.sys_com('USE_TF_KERAS=1')
            self.sys_com('python setup.py install')
            import tensorflow as tf
            tf.__version__     
        # custom setup stuff for gallery-dl repo
        if 'mikf/gallery-dl' in self.repo_list:
            os.chdir(self.git_install_root+'/gallery-dl')
            self.sys_com("pip install -e . |grep 'succes'",True)
        # custom setup stuff for youtube-dl repo
        if 'ytdl-org/youtube-dl' in self.repo_list:
            os.chdir(self.git_install_root+'/youtube-dl') 
            self.sys_com("pip install -e . |grep 'succes'",True)      
        # switch backt to root
        os.chdir(self.git_install_root)
        
    #   --grab the username if a repos is installed
    #   --generate a txt file of all other reps of the user    
    def get_other_reps(self):          
        for r in self.repo_list:
            self.GitUsers=[]
            self.sub_repo_list=[]
            self.GUSER=r.split('/')[0]
            self.repo_name=r.split('/')[1]
            self.GitUsers.append(self.GUSER)
            h=Helpers()

            CURL_CMD="curl https://api.github.com/users/{self.GUSER}/repos?per_page=100 | grep -o '"
            CURL_CMD+='git@[^"]*' + ' > '+self.git_install_root+'/info.txt'
            result=self.sys_com(CURL_CMD)
            print(result)
            self.sys_com('cat '+self.git_install_root+"/info.txt |awk -F ':' '{print $2}'|awk -F '.' '{print $1}' > "+self.path+"/"+self.GUSER+"_repositories.txt")
            with open(self.git_install_root+'/info.txt','r') as f:
                for line in f:
                    cline=line.split(':')[1].split('.')[0]
                    self.sub_repo_list.append(cline),

        print(self.sub_repo_list)

    # END OF HELPER FUNCTIONS
  
    def no_action(self):
        return self._vdir()
        
def get_hmm():
    """Get a thought."""
#     help(ZipUp)
    return 'hmmm...'

def hmm(tool):
    """Contemplation..."""
    print( helpers.get_answer() )
    if helpers.get_answer():
        print(get_hmm())

# def ZipUp(zipname, foldername, target_dir): 
#     """zips a folder and uploads it to gdrive"""
#     Zipup.ZipUp(zipname, foldername, target_dir)
