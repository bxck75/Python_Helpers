import os, sys, inspect
from pathlib import Path
import Helpers

class main:
    ''' This and the core.py file are the main frontier of development '''
    def __init__(self):
        ''' set root paths '''
        self.root = '/content'
        self.gdrive_root = '/content/drive/My Drive'
        self.helpers_root = self.root + '/installed_repos/Python_Helpers'

        ''' import helpers '''
        os.chdir(self.helpers_root)
        
        ''' start helper core and system commands '''
        self.Helpers_Core=Helpers.Core() # new helper class
        self.HelpMe = Helpers.BigHelp.Helpers # build in system commands old  module helpers
        self.Sys_Exec = self.Helpers_Core.Sys_Exec # execute system command

        ''' Better chdir '''
        self.c_d = self.Helpers_Core.cd
        self.c_d(self.root)
        
        ''' scraper install '''
        self.c_d(self.root)
        
        ''' In_helpers/helpers/ map ''' 
        inst_dir=self.helpers_root+'/Helpers'
        repos=['bxck75/piss_ant_pix2pix','bxck75/A1Colabs']
        self.Helpers_Core.install_repos(repos, inst_dir,False,True)

        ''' cv2 and distro install '''
        cv_repos=[
            'bxck75/opencv_contrib',
            'bxck75/opencv',
            'bxck75/face2face-demo',
            'bxck75/face-recognition',
        ]
        self.Helpers_Core.install_repos(cv_repos, inst_dir,False,True) 
        
        ''' needed gdrive repos '''
        gdrive_rps=[
            'bxck75/google-drive-list-shared', 
            'bxck75/PyDrive'
        ]
        self.Helpers_Core.install_repos(gdrive_rps, inst_dir,False,True)

        ''' PyDrive install '''
        self.Sys_Exec('python /content/installed_repos/Python_Helpers/Helpers/PyDrive/setup.py install')
        import pydrive
        self.pydr= pydrive
        
        ''' google shared wrapper '''
        self.Sys_Exec('cp ' + self.helpers_root + '/Helpers/google-drive-list-shared/google-drive-list-shared.py ' + self.helpers_root + '/Helpers/gdrive_shared.py')
        self.Sys_Exec('rm -r ' + self.helpers_root + '/Helpers/google-drive-list-shared')

        ''' pix2pix repos '''
        pix2pix_rps=['bxck75/piss-ant-pix2pix','bxck75/dosage']
        self.Helpers_Core.install_repos(pix2pix_rps, inst_dir,False,True)
        
main()
