import os, sys, inspect
import Helpers

class main:
    
    def __init__(self):
        
        ''' set root paths '''
        self.root = '/content'
        self.gdrive_root = '/content/drive/My Drive'
        self.helpers_root = self.root + '/installed_repos/Python_Helpers'

        ''' import helpers '''
        os.chdir(self.helpers_root)
        
        ''' start helper core and system commands '''
        self.Helpers_Core=Helpers.Core() # new helper class
        self.hlp=self.Helpers_Core.H  # old  module helpers
        self.HelpMe = self.Helpers_Core.H.Me # build in system commands old  module helpers
        self.Sys_Exec = self.Helpers_Core.Sys_Exec

        ''' Better chdir '''
        self.c_d = self.Helpers_Core.cd
        self.c_d(self.root)
        
        ''' scraper install '''
        self.c_d(self.root)
        self.dosage = ['bxck75/dosage']
        self.HelpMe(['inst_reps', self.dosage,  self.helpers_root+'/Helpers', False, True])

        ''' needed gdrive repos '''
        self.gd_rps=[
            'bxck75/google-drive-list-shared',
            'bxck75/PyDrive',
        ]
        self.HelpMe(['inst_reps',self.gd_rps, self.helpers_root+'/Helpers',False,True])

        ''' PyDrive install '''
        self.Sys_Exec('python /content/installed_repos/Python_Helpers/Helpers/PyDrive/setup.py install')
        import pydrive

        ''' google shared wrapper '''
        self.Sys_Exec('cp ' + self.helpers_root + '/Helpers/google-drive-list-shared/google-drive-list-shared.py ' + self.helpers_root + '/Helpers/gdrive_shared.py')
        self.Sys_Exec('rm -r ' + self.helpers_root + '/Helpers/google-drive-list-shared')

        ''' pix2pix repos '''
        self.pix2pix_rps=[
            'bxck75/piss-ant-pix2pix',
            'bxck75/scrape-linkedin-selenium',
            # 'bxck75/opencv',
            ]
        self.HelpMe(['inst_reps',self.pix2pix_rps, self.root +'/installed_repos',False,True])

        ''' many repos in this list!!! '''
        self.Helpers.RepCoList.repos_sorted

        ''' zipper init '''
        self.Zipper = self.Helpers_Core.load_zipper()

        ''' gdrive downloader init '''
        self.Gdrive_download = self.Helpers_Core.Gdownload.GdriveD

        ''' image crawler init'''
        self.ImgCrawler = self.Helpers.core.GoImgScrape.GoogleImageCrawler()
        
M = main()
