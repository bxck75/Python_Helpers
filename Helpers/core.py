# -*- coding: utf-8 -*-
import os,sys
from . import helpers
from . import ZipUp
from . import BigHelp
from . import RepCoList
from . import custom_functions
from . import resize
from . import GdriveD
from . import logger

class Core:
    '''
    --- Examples for Colab
        # remove defaults
        !rm -r sample_data
        # Clone the frame
        !git clone https://github.com/bxck75/Python_Helpers.git
        # Change dir
        %cd /content/Python_Helpers
        # install
        !python setup.py install
        import main
        import os
        import sys
        import IPython
        from IPython.display import clear_output
        # Load the core helper object
        D=main.Helpers.core.Core()
        clear_output()
     ---
     ---
        # x=dir(D)
        D.landmark_face = D.H.landmarkdetect
        D.H.Me(['vdir',[D.H.landmarkdetect]])
        D.H.Me(['flickr',['portrait'],'images',10])
        # dir(D.H.landmarkdetect)
        # print(x)
     ---
     ---
        # random demo of some functionality
        M=main
        M.root_dirname, M.root_filename = os.path.split(os.path.abspath(M.__file__))
        M.help = M.Helpers.BigHelp.Helpers()
        M.logger = M.Helpers.logger
        M.zip_to_drive = M.Helpers.ZipUp
        M.all_repos = M.Helpers.RepCoList
        M.download_gdrive_file = M.Helpers.GdriveD
        M.resize_folder = M.Helpers.resize.resize_folder
        # M.image_process = M.Helpers.process

        # logger
        M.logger.get_logger('Debug_Log',str(M.root_dirname)+'/debug_log.txt',True)
        M.logger.logging.basicConfig()
        M.logger.logging.log(1,'TestLog')

        # M.training_set_builder 
        M.reps_to_install=['bxck75/piss-ant-pix2pix','affinelayer/pix2pix-tensorflow']
        M.help.Me(['inst_reps',M.reps_to_install,str(M.root_dirname)+'/pix2pix_repos',False,True])
        # M.help.Me(['inst_reps',M.all_repos.reps,'/content/all_ml_repos',True,True])
     ---
     ---

                 def setmaker(_in_,_mode_,_out_):
        #     global r
            M.help.Me(['cml','python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(M.root_dirname)+'/images_resized'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(M.root_dirname)+'/images_resized')
            M.help.Me(['cml','echo python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation blank --output_dir '+str(M.root_dirname)+'/images_blank'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation blank --output_dir '+str(M.root_dirname)+'/images_blank')
            M.help.Me(['cml','echo python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation edge --output_dir '+str(M.root_dirname)+'/images_edge'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation edge --output_dir '+str(M.root_dirname)+'/images_edge')

            if _mode_ != '':
                M.help.Me(['cml','echo python ' + str(M.root_dirname)+'/tools/process.py --input_dir ' + str(M.root_dirname)+'/images_' + _mode_ +' --operation combine --output_dir ' + str(_out_)])
        #         os.system('echo python ' + str(M.root_dirname)+'/tools/process.py \
        #             --input_dir ' + str(M.root_dirname)+'/images_' + _mode_ + ' \
        #             --operation combine \
        #             --output_dir ' + str(_out_))

        M.setmaker = setmaker
        # M.setmaker.mode_type = 'edge' # blank
        # M.setmaker.img_dir = str(M.root_dirname)+'/images'
        # M.setmaker.final_set_dir = str(M.root_dirname)+'/images_set'
        # print(M.setmaker)
        M.setmaker(str(M.root_dirname)+'/images', 'edge', str(M.root_dirname)+'/images_set')

     ---
    '''
    def __init__(self):
        '''int objects'''
        self.root_dirname, self.root_filename = os.path.split(os.path.abspath(__file__))
        self.H = self.load_helpers()
        self.H.zip = self.load_zipper()
        self.H.flickr_scr = self.flickr_scrape
        self.H.setmaker = self.set_maker
        
    def load_helpers(self):
        '''load BigHelp to gdrive obj'''
#         self.C = BigHelp
        return BigHelp.Helpers()

    def load_zipper(self):
        '''load zipup to gdrive obj'''
#         self.C = BigHelp
        return ZipUp.ZipUp

    def set_maker(_in_,_mode_,_out_):
        '''
           set_maker(_in_,_mode_,_out_):
        '''
        #     global r
        self.H.Me(['cml','python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(self.root_dirname)+'/images_resized'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(_in_)+' --operation resize --output_dir '+str(M.root_dirname)+'/images_resized')
        self.H.Me(['cml','echo python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(self.root_dirname)+'/images_resized --operation blank --output_dir '+str(self.root_dirname)+'/images_blank'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation blank --output_dir '+str(M.root_dirname)+'/images_blank')
        self.H.Me(['cml','echo python '+str(self.root_dirname)+'/tools/process.py --input_dir '+str(self.root_dirname)+'/images_resized --operation edge --output_dir '+str(self.root_dirname)+'/images_edge'])
        #     os.system('python '+str(M.root_dirname)+'/tools/process.py --input_dir '+str(M.root_dirname)+'/images_resized --operation edge --output_dir '+str(M.root_dirname)+'/images_edge')
        if _mode_ != '':
            self.H.Me(['cml','echo python ' + str(self.root_dirname)+'/tools/process.py --input_dir ' + str(self.root_dirname)+'/images_' + _mode_ +' --operation combine --output_dir ' + str(_out_)])
        #         os.system('echo python ' + str(M.root_dirname)+'/tools/process.py \
        #             --input_dir ' + str(M.root_dirname)+'/images_' + _mode_ + ' \
        #             --operation combine \
        #             --output_dir ' + str(_out_))

    def flickr_scrape(self,search_list,img_dir,qty):
        '''
             #get 20 images from flickr
             img_dir='images'
             qty=10
             search_list = ['portait','face']
             flickr_scrape(self,search_list,img_dir,qty): 
        '''
        self.H.Me(['flickr',search_list,str(self.root_dirname)+'/'+img_dir,qty])
        # see if they are downloaded
        img_list = self.H.Me(['globx',str(self.root_dirname)+'/images','*.jpg'])
        print(len(img_list))
        # M.resize.resize_folder(str(M.root_dirname)+'/images')
        i=0
        # self.H.Me(['cml','rm -r '+str(M.root_dirname)+'/images'])
        for img in img_list:
            print(img)
            self.H.Me(['cml','cp '+img+' '+str(self.root_dirname)+'/images/img_%d.jpg'%(i+1)])
            i+=1
        print(str(i)+' images copied!')
        self.H.Me(['cml','rm -r '+str(self.root_dirname)+'/images/flickr'])


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
