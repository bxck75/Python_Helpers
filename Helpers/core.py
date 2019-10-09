s# -*- coding: utf-8 -*-
import os, sys, inspect
os.system('pip install colorama')
import colorama

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


class Core:
    '''
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

    '''
    def __init__(self):
        
        self.root_dirname, self.root_filename = os.path.split(os.path.abspath(__file__))    # local root
        self.Colab_root = '/content'
        self.helpers_root = self.Colab_root + '/installed_repos/Python_Helpers/Helpers'
        self.root = self.Colab_root                                                         # absolute root
        self.git_install_root = self.Colab_root + '/installed_repos'                        # git install root
        self.Gdrive_root= self.Colab_root+ '/drive/My Drive'                                # google drive root

        
        # inject functionality into the object
        self.BigHelp =      BigHelp
        self.Ops =          ops
        self.Repo_List =    RepCoList
        self.ColorPrint =   ColorPrint
        self.GdriveD =      GdriveD
        self.FileView =     Fileview
        self.ZipUp =        ZipUp
        self.ImgCrawler =   GoImgScrape
        self.GooScrape =    gscrape
        self.Resize =       resize 
        self.Logger =       logger
        self.ImgTools =     Img.Tools
        
        ''' Init a few modules '''
        self.ImgCrawler.GoogleImageCrawler()
        ''' flickr scraper '''
        self.FlickrS = self.flickr_scrape
        ''' Many repos in this list!!! '''
        self.sorted_repos = self.Repo_List.repos_sorted
        ''' Sys.exec en sys.log '''
        self.Sys_Exec = self.sys_com
        self.LogGER = self.sys_log
        ''' Better change dir '''
        self.c_d = self.cd       
        ''' Change to root folder '''
        self.c_d(self.root)
        # existencecheker
        self.if_exists = os.path.exists
        
        # cd root
        self.c_d(self.root)
        print('classes shuffle done!')
        
        ''' handpicked repos '''
#         self.handpicked_repos = self.sorted_repos
#         print(self.handpicked_repos)
#         self.Helpers_Core.install_repos(handpicked_repos, inst_dir)
#         self.HelpMe(['inst_reps',self.handpicked_repos, self.root +'/installed_repos',False,True])

        ''' In_helpers/helpers/ map ''' 
        inst_dir=self.helpers_root+'/Helpers'
        repos=[
            'bxck75/piss_ant_pix2pix',
            'bxck75/A1Colabs',
        ]
        r = self.install_repos(repos, inst_dir,False,True)
        print(r)
        ''' cv2 and distro install '''
        cv_repos = [
            'bxck75/opencv_contrib',
            'bxck75/opencv',
            'bxck75/face2face-demo',
            'bxck75/face-recognition',
        ]
        r =self.install_repos(cv_repos, inst_dir, False, True) 
        print(r)

        ''' needed googledrive repos '''
        gdrive_rps=[
            'bxck75/google-drive-list-shared', 
            'bxck75/PyDrive'
        ]
        r = self.install_repos(gdrive_rps, inst_dir, False, True)
        print(r)
    
        ''' PyDrive install '''
        sr = self.Sys_Exec('python /content/installed_repos/Python_Helpers/Helpers/PyDrive/setup.py install')
        import pydrive
        
        ''' google shared wrapper '''
        sr += self.Sys_Exec('cp ' + self.helpers_root + '/Helpers/google-drive-list-shared/google-drive-list-shared.py ' + self.helpers_root + '/Helpers/gdrive_shared.py')
        sr += self.Sys_Exec('rm -r ' + self.helpers_root + '/Helpers/google-drive-list-shared')

        ''' pix2pix repos '''
        pix2pix_rps=[
                'bxck75/piss-ant-pix2pix',
                'bxck75/dosage',
        ]
        r=self.install_repos(pix2pix_rps, inst_dir,False,True)
        print(r)

        
    '''###################################################################################################'''   
    '''                               Definitions bellow this line                                        '''
    '''                                   existence checker                                               '''
    def haar_detect(self, img):
        ''' detect faces
        import matplotlib.pyplot as plt
        import sys
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
        plt.show
        
        
    def DelDig(self, list): 
        '''
            # Driver code  
            # https://gist.githubusercontent.com/bxck75/dc0ef99833af8a2b2533c2d1634d24d0/raw/212feb5df1f89e1f2bce1e8b3c0c10015f875e93/DelDig.py
        '''
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
            elif mode == 'symantic':
                ''' other processes to make set '''
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
        img = cv.imread(input_path)
        if img is None:
            print('Failed to load image file:', input_path)
            sys.exit(1)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        lsd = cv.line_descriptor_LSDDetector.createLSDDetector()
        lines = lsd.detect(gray, 1, 1)
        for kl in lines:
            if kl.octave == 0:
                # cv.line only accepts integer coordinate
                pt1 = (int(kl.startPointX), int(kl.startPointY))
                pt2 = (int(kl.endPointX), int(kl.endPointY))
                cv.line(img, pt1, pt2, [255, 0, 0], 2)
                
        print(output_path)
        cv.imwrite(output_path, img)
        
        
        
    def install_repos(self, repos, inst_dir, sub_repos=False, chadir=False):
        '''
        Example:
            inst_dir='/content/images'
            repos=['bxck75/piss_ant_pix2pix','bxck75/opencv']
            install_repos(repos, inst_dir)
        '''
#         self.repo_list=repos      
#         self.git_install_root=inst_dir
#         self.sub_repos=sub_repos
#         self.chadir=chdir
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


    def GlobX(self, path_in, pattern_in):
        ''' Glob folders on pattern '''
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
#         self.flickr_dest = dest
#         self.flickr_qty = qty
#         self.flickr_query = query
#         root='/content'
        if (query != '' and qty != '' and dest != '' ):
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
        
        
#     def _flickr(self):
#         '''
#             Internal function for flickr_scrape
#             _flickr(flickr_query, flickr_dest='/content/images', flickr_qty=10)
#         '''
#         os.system('sudo pip install gallery-dl')
#         if isinstance(self.flickr_query, list):
#             for s in self.flickr_query:
#                 keyword=s.replace(' ', '+')
#                 self.sys_com('gallery-dl --range 1-'+str(self.flickr_qty)+' -d '+self.flickr_dest+' https://flickr.com/search/?text='+keyword)
#         else: 
#             keyword=str(self.flickr_query.replace(' ', '+'))
#             self.sys_com('gallery-dl --range 1-'+str(self.flickr_qty)+' -d '+self.flickr_dest+' https://flickr.com/search/?text='+keyword)

            
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
        '''
            validate list if not empty
            valid_list(self, lst)
        '''
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
            
        def __repr__(self):
            return self.path
        
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
