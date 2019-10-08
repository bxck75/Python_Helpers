import os, sys, inspect
import Helpers

class main:
    
    def __init__(self):
        
        ''' set root paths '''
        root = '/content'
        gdrive_root = '/content/drive/My Drive'
        helpers_root = root + '/installed_repos/Python_Helpers'

        ''' import helpers '''
        os.chdir(helpers_root)
        
        ''' start helper core and system commands '''
        Helpers_Core=Helpers.Core() # new helper class
        hlp=Helpers_Core.H  # old  module helpers
        HelpMe = Helpers_Core.H.Me # build in system commands old  module helpers
        Sys_Exec = Helpers_Core.Sys_Exec

        ''' Better chdir '''
        c_d = Helpers_Core.cd
        c_d(root)
        
        ''' scraper install '''
        c_d(root)
        dosage = ['bxck75/dosage']
        HelpMe(['inst_reps', dosage,  helpers_root+'/Helpers', False, True])

        ''' needed gdrive repos '''
        gd_rps=[
            'bxck75/google-drive-list-shared',
            'bxck75/PyDrive',
        ]
        HelpMe(['inst_reps',gd_rps, helpers_root+'/Helpers',False,True])

        ''' PyDrive install '''
        Sys_Exec('python /content/installed_repos/Python_Helpers/Helpers/PyDrive/setup.py install')
        import pydrive

        ''' google shared wrapper '''
        Sys_Exec('cp ' + helpers_root + '/Helpers/google-drive-list-shared/google-drive-list-shared.py ' + helpers_root + '/Helpers/gdrive_shared.py')
        Sys_Exec('rm -r ' + helpers_root + '/Helpers/google-drive-list-shared')

        ''' pix2pix repos '''
        pix2pix_rps=[
            'bxck75/piss-ant-pix2pix',
            'bxck75/scrape-linkedin-selenium',
            # 'bxck75/opencv',
            ]
        HelpMe(['inst_reps',pix2pix_rps, root +'/installed_repos',False,True])

        ''' many repos in this list!!! '''
        Helpers.RepCoList.repos_sorted

        ''' zipper init '''
        Zipper = Helpers_Core.load_zipper()

        ''' gdrive downloader init '''
        Gdrive_download = Helpers_Core.Gdownload.GdriveD

        ''' image crawler init'''
        ImgCrawler = Helpers.core.GoImgScrape.GoogleImageCrawler()
        
M = main()
