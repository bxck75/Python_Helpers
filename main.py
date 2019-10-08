import os, sys, inspect
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
        self.hlp=Helpers.BigHelp.Helpers  # old  module helpers
        self.HelpMe = Helpers.BigHelp.Helpers.Me # build in system commands old  module helpers
        self.Sys_Exec = self.Helpers_Core.Sys_Exec # execute system command

        ''' Better chdir '''
        self.c_d = self.Helpers_Core.cd
        self.c_d(self.root)
        
        ''' scraper install '''
        self.c_d(self.root)
#         self.HelpMe(['inst_reps', ['bxck75/dosage'], self.helpers_root+'/Helpers', False, True])
        
        ''' cv2 and distro install '''
        cv_repos=[
            'bxck75/opencv_contrib',
            'bxck75/opencv',
            'bxck75/face2face-demo',
            'bxck75/face-recognition',
        ]
#         self.HelpMe(['inst_reps', cv_repos,  self.helpers_root+'/Helpers', False, True])

        ''' needed gdrive repos '''
        gdrive_rps=[
            'bxck75/google-drive-list-shared', 
            'bxck75/PyDrive'
        ]
#         self.HelpMe(['inst_reps',gdrive_rps, self.helpers_root+'/Helpers',False,True])

        ''' PyDrive install '''
        self.Sys_Exec('python /content/installed_repos/Python_Helpers/Helpers/PyDrive/setup.py install')
        import pydrive
        self.pydr= pydrive
        
        ''' google shared wrapper '''
        self.Sys_Exec('cp ' + self.helpers_root + '/Helpers/google-drive-list-shared/google-drive-list-shared.py ' + self.helpers_root + '/Helpers/gdrive_shared.py')
        self.Sys_Exec('rm -r ' + self.helpers_root + '/Helpers/google-drive-list-shared')

        ''' pix2pix repos '''
        pix2pix_rps=['bxck75/piss-ant-pix2pix']
#         self.HelpMe(['inst_reps',pix2pix_rps, self.root +'/installed_repos',False,True])

        ''' many repos in this list!!! '''
        self.sorted_repos = Helpers.RepCoList.repos_sorted.sort()
        
        ''' handpicked repos '''
#         handpicked_repos = self.sorted_repos[:8]
#         print(self.handpicked_repos)
#         self.HelpMe(['inst_reps',self.handpicked_repos, self.root +'/installed_repos',False,True])

        ''' zipper init '''
        self.Zipper = self.Helpers_Core.load_zipper()

        ''' gdrive downloader init '''
        self.Gdrive_download = self.Helpers_Core.Gdownload.GdriveD

        ''' image crawler init'''
        self.ImgCrawler = Helpers.core.GoImgScrape.GoogleImageCrawler()
        
main()
