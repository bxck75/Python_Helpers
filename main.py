import os, sys, inspect
from pathlib import Path
import Helpers

os.system('pip install icrawler')

class main:
    ''' This and the core.py file are the main frontier of development '''
    def __init__(self):
        ''' set root paths '''
        self.root = '/content'
        self.gdrive_root = self.root + '/drive/My Drive'
        self.helpers_root = self.root + '/installed_repos/Python_Helpers'
        os.chdir(self.helpers_root)
        
        ''' start helper core and system commands '''
        self.Helpers_Core=Helpers.Core() # new helper class
        self.HelpMe = Helpers.BigHelp.Helpers # build in system commands old  module helpers
        self.Sys_Exec = self.Helpers_Core.Sys_Exec # execute system command
 
