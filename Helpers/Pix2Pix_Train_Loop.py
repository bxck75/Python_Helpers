import sys
import os
import dlib
import glob
%matplotlib inline
from matplotlib import pyplot as plt
import cv2
''' 
    loop  10x
    1 get metric from gdrive
    2 train 5 epochs
    3 dump metrics to gdrive with the same file id 
'''
%tensorboard --logdir /content/metrics
for i in range(1):
    ''' fetch metrics'''
    %cd /content/
    Helpers.GdriveD.GdriveD(images_model_code, '/content/'+images_set_name+'_model_in.zip')
    !unzip /content/{images_set_name}_model_in.zip -d metrics/

    ''' train epochs '''
    %cd /content/installed_repos/piss-ant-pix2pix
    !python pix2pix.py --checkpoint /content/metrics --output_dir /content/metrics --progress_freq 50 --save_freq 50 --summary_freq 50 --display_freq 250 --max_epochs 3 --mode train --input_dir /content/{images_set_name}images/_combined/train --which_direction 'BtoA'

    %cd /content/
    '''clean old models,test images,logs etc befor zipping'''
    # delete unwanted
    !rm -r /content/metrics/index.html

    # clean up images
    img_list=hlp.Me(['globx','/content/metrics/images','*.*g'])
    img_list = sorted(img_list)
    print(img_list)
    n=6 #pop the last 6 items off the list (latest images)
    latest = img_list[-n:]
    for i in range(n):
        img = dlib.load_rgb_image(latest[i]) 
        plt.imshow(img)
        plt.show()
    del img_list[-n:]
    # delete the files left in the list
    for i_file in img_list:
        print('deleting : ' + i_file)
        !rm -r {i_file}

    # clean up models
    models_list=hlp.Me(['globx','/content/metrics','model-*'])
    models_list = sorted(models_list)
    print(models_list)
    n=6 #pop the last 6 items off the list (latest model)
    del models_list[-n:]
    # delete the files left in the list
    for m_file in models_list:
        print('deleting : ' + m_file)
        !echo rm -r {m_file}
    # clean up events
    events_list=hlp.Me(['globx','/content/metrics','events*'])
    events_list = sorted(events_list)
    print(events_list)
    n=3 #pop the last item off the list (latest event) 
    del events_list[-n:]
    # delete the files left in the list
    for e_file in events_list:
        print('deleting : ' + e_file)
        !echo rm -r {e_file}

    ''' zip metrics up to gdrive '''
    %cd /content/
    Helpers.Core()
    obj=Helpers.core.Core()
    folder_of_model='metrics'
    result=obj.H.zip(images_set_name+'model',obj.Gdrive_root+'/models',folder_of_model).ZipUp
    zip_hash=result.split('(id) ')[1]
    print(zip_hash)

    # delete old metrics before unpacking new in the beginning of the loop
    # !rm -r /content/metrics
    !rm -r /content/{images_set_name}model.zip
