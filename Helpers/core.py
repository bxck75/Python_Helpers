# -*- coding: utf-8 -*-
import os, sys, inspect
os.system('pip install colorama')
import colorama

from . import helpers
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
from . import ICrawl
# from . import Scraper

class Core:
    '''
        New help will be made later .......
        Functions:
        
         'MethHelp',
         'cd',
         'cdr',
         'check_img_list',
         'docu',
         'explore_mod',
         'flickr_scrape',
         'get_gdrive_dataset',
         'img_batch_rename',
         'into_func',
         'loadTboard',
         'load_helpers',
         'load_zipper',
         'rec_walk_folder',
         'set_maker',
         'valid_img',
         'valid_list'
         
        Examples:

            import os
            # remove defaults
            os.system('rm -r sample_data')
            
            # Clone the repo
            os.system('git clone https://github.com/bxck75/Python_Helpers.git')


            # Change dir
            os.chdir('/content/Python_Helpers')
            
            # install
            os.system('python setup.py install')

            from IPython.display import clear_output
            from PIL import Image
            import main
            import sys
            import IPython
            import Helpers
            
            # set few helper objects
            P=Helpers.core.Core()
            hlp=P.H
            os.chdir('/content/')
            hlp.repolist= hlp.repo_collection
            repos_sorted = hlp.repo_collection.repos_sorted
            
            # get pix2pix repo
            A1=['bxck75/piss-ant-pix2pix']
            hlp.Me(['inst_reps',A1,'/content/installed_repos',False,True])
            
            # Dir Module
            hlp.Me(['vdir',Helpers])
            # Explore modules classes and functions
            Helpers.Core().docu('os','system')
            
     ---
    '''
    def __init__(self):
        '''int objects'''
        self.root_dirname, self.root_filename = os.path.split(os.path.abspath(__file__))
        self.Colab_root = '/content'
        self.Gdrive_root= self.Colab_root+ '/drive/My Drive'  
        self.Gdownload = GdriveD
        self.H = self.load_helpers()
        self.H.zip = self.load_zipper()
        self.H.repo_collection = RepCoList
        self.H.flickr_scr = self.flickr_scrape
        self.Sys_Exec = self.sys_com
        self.Log = self.Sys_Exec
        self.if_exists = os.path.exists
        self.icrawl = ICrawl.ICrawl
    
    def cprint(self, msg, style='info'):
        ''' set color output '''
        mod, meth, func = 'ColorPrint','ColorPrint','print_'+style
        cprint_func = self.info_func(mod, meth, func)
        cprint(msg)
#         self.print_fail = ColorPrint.ColorPrint.print_fail
#         self.print_pass = ColorPrint.ColorPrint.print_pass
#         self.print_warn = ColorPrint.ColorPrint.print_warn
#         self.print_info = ColorPrint.ColorPrint.print_info
#         self.print_bold = ColorPrint.ColorPrint.print_bold
    
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
        self.system_log_file = self.Colab_root + '/' + log_name + '.txt'

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
                          
        # log 
        log_msg = str(self.Sys_Cmd)
        func_name=inspect.stack()[0][3]
        self.sys_log(func_name + '<~[LOGGED]~>' + log_msg )                          
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
        # log 
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
        from PIL import Image
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
        log_msg = str([keep, cleanup_path, search_pattern])
        func_name = str(inspect.stack()[0][3])
        self.sys_log( func_name + '<~[LOGGED]~>' + log_msg )
             
        import dlib
        import matplotlib.pyplot as plt
        # clean up images
        img_list = self.H.Me(['globx', cleanup_path, search_pattern])
        img_list = sorted(img_list)
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
