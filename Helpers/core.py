# -*- coding: utf-8 -*-
from . import helpers
from . import ZipUp
from . import BigHelp
from . import RepCoList
from . import custom_functions
from . import resize
from . import GdriveD
from . import logger

class Core:
    
    def __init__(self):
        pass
    
    def load_helpers(self):
        BH = BigHelp.Helpers()
        print('here')     


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
