# -*- coding: utf-8 -*-
import os,sys
from . import helpers
from . import ZipUp
from . import BigHelp
from . import RepCoList
from . import resize
from . import GdriveD
from . import logger
from . import GoImgScrape

# from . import process


from . import ops

class Core:
    '''
                                ['Me',
                             '_cml',
                             '_flickr',
                             '_get_args',
                             '_get_gpu',
                             '_globx',
                             '_inst_reps',
                             '_methods_of',
                             '_mkd',
                             '_pip',
                             '_vdir',
                             'args',
                             'custom_reps_setup',
                             'flickr_dest',
                             'flickr_qty',
                             'flickr_query',
                             'flickr_scr',
                             'get_other_reps',
                             'landmarkdetect',
                             'landmarkdetecter',
                             'method',
                             'method_args',
                             'no_action',
                             'root_path',
                             'zip']
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
        self.Gdrive_root= '/content/drive/My Drive'
        self.Gdownload = GdriveD
        self.H = self.load_helpers()
        self.H.zip = self.load_zipper()
        self.H.repo_collection = RepCoList
        self.H.flickr_scr = self.flickr_scrape
                
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
            return rec_walk_folder(dir)

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
            print('deleting '+ i.format)
            os.remove(filename)
            return False

    def valid_list(self, lst):
        ''' validate list if not empty'''
        if len(lst) > 0:
            return True
        else:
            return False

    def check_img_list(self, img_list, ext='png'):
        '''
            check images list and remove bad files 
                check_img_list((img_list, ext='png')
        '''
        img_list = sorted(img_list)
        print('[checking images list')
        if valid_list(img_list):
            for f in img_list:
                if not valid_img(f,ext):
                    os.remove(f)
    
    def dir_rec(self, meth, rec_lvl=1,count=0):
        '''
            recusive dir on modules to discover methods and sub-methods
                dir_rec(meth, rec_lvl=1)
        '''
        self.count=count
        self.recuring_lvls = rec_lvl
        
        '''set root entry in dict'''
        if self.count <= self.recuring_lvls:
            if self.count == 0:
                self.dir_list = {}
#             else:
#                 self.dir_list = self.dir_list
        
            self.dir_list[str(meth)] = {}  
            self.dir_list[str(meth)]['lvl_' + str(0)] = {}
            self.dir_list[str(meth)]['lvl_' + str(0)] = self.H.Me(['vdir',meth])
        
            self.count += 1
#         for lvl in range(1,self.recuring_lvls):   
            self.dir_list[str(meth)]['lvl_' + str(count+1)] = {}
            if self.valid_list(self.dir_list[str(meth)]['lvl_' + str(count)]):
               for i in range(1,len(self.dir_list[str(meth)]['lvl_' + str(count)])):
                   print(i)
                   print(count)
                   print(len(self.dir_list[str(meth)]['lvl_' + str(count)]))
                   child_meth = self.dir_list[str(meth)]['lvl_' + str(count)][i-1]
                   print(child_meth)

                   self.dir_list[meth.__name__]['lvl_' + str(count+1)][child_meth]={}
                   self.dir_list[meth.__name__]['lvl_' + str(count+1)][child_meth]['lvl_' + str(0)] = self.H.Me([ 'vdir', meth+'.'+child_meth ])                       
                   self.dir_rec(meth+'.'+child_meth,count=self.count)    
            else:
                print('not a valid list')
            
        return self.dir_list
    
      
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
        self.H.Me(['cml','cp -r '+pack+' '+self.root_dirname+self.H.DS_ROOT])
        os.chdir(self.root_dirname+self.H.DS_ROOT)
        self.H.Me(['cml','unzip -q '+pack])
        self.H.Me(['cml','rm -r '+pack])
        os.chdir(self.root_dirname)

    def MethHelp(self,libs):
        os_help=self.H.Me(['vdir',libs])
        #make a list containing libs values of os_help
        listOfLibs = [x[0] for x in os_help]
        #make a list containing libs method values of os_help
        listOfMethods= [x[1] for x in os_help]
        # Create a zipped list of tuples from above lists
        zippedList =  list(zip(listOfLibs, listOfMethods[0:5]))
        zippedList
        # request help on method from list
        return zippedList

    def loadTboard():
        '''load tensorboard'''
        import datetime, os ,tensorboard 
        
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

    def flickr_scrape(self,query= ['portrait'],qty=5,dest='/content/images'):
        '''
            search_list,img_dir,qty
            #get 20 images from flickr
            img_dir='images'
            qty=10
            search_list = ['portait','face']
            flickr_scrape(self,search_list,img_dir,qty): 
            # print(self.flickr_dest)
            # print(self.flickr_qty)
            # print(self.flickr_query)
        '''
        self.flickr_dest = dest
        self.flickr_qty = qty
        self.flickr_query = query
        
        root='/content'
        if (self.flickr_query != '' and self.flickr_qty != '' and self.flickr_dest != '' ):
            self.H.Me(['flickr',self.flickr_query,self.flickr_dest, self.flickr_qty])
        # see if they are downloaded
        img_list = self.H.Me(['globx',str(self.flickr_dest),'*.jpg'])
        print(len(img_list))
        # M.resize.resize_folder(str(M.root_dirname)+'/images')
        i=0
        # self.H.Me(['cml','rm -r '+str(M.root_dirname)+'/images'])
        for img in img_list:
            print(img)
#             self.H.Me(['cml','cp '+img+' '+str(self.root_dirname)+'/images/img_%d.jpg'%(i+1)])
            self.H.Me(['cml','cp '+img+' '+str(self.flickr_dest)+'/img_%d.jpg'%(i+1)])      
            i+=1
        print(str(i)+' images copied!')
        self.H.Me(['cml','rm -r '+str(self.flickr_dest)+'/flickr'])


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
