from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# Helpers Loading
from pathlib import Path
lib_file=Path('/content/lib/Helpers.py')
if not lib_file.is_file():
    import os, inspec
    os.system('mkdir -p /content/lib')
    os.chdir('/content/lib')
    os.system('wget https://raw.githubusercontent.com/bxck75/Helpers/Helpers.py')
    from lib.Helpers import Helpers
    os.chdir('/content/')
resmon_file = Path('/content/lib/resource_monitor.py')
if not  resmon_file.is_file():
    os.system('wget https://github.com/googlecolab/colabtools/blob/master/google/colab/_serverextension/_resource_monitor.py -O /content/lib/resource_monitor.py')

# regular imports
from fastai.vision import *
from fastai.vision.gan import *
import seaborn as sns
import numpy as np
import pandas as pd
import fastai, hashlib
from IPython.display import clear_output
from IPython import display

# Init helpers
H=Helpers()
# delete standaard data
H.Me(['cml','rm -r /content/sample_data'])
# ever growing class of helpers
# This needs https://github.com/bxck75/PyHelpers.git
H.Me(['inst_reps',[bxck75/Helpers],'/content/lib',True,True])
# Now that the repo is pulled
from PyHelpers.Helpers import Helpers as Help # general helpers
from PyHelpers.GdriveD import GdriveD as GD #Gdrive downloader
from PyHelpers.RepCoList import reps as R # huge list of found repos
from PyHelpers.ZipUp import zipfolder as zipr # zip and upload to gdrive

''' Functions define '''
def get_gdrive_dataset(pack, DS_root='datasets',GD_root='datasets'):
    import google
    from google.colab import drive
    drive.mount('/content/drive', force_remount=True)
    H.GD_ROOT=GD_root+'/'
    H.DS_ROOT=DS_root+'/'
    os.chdir(H.gdrive_root+H.GD_ROOT)
    H.Me(['mkd',[DS_root,'models'],H.pix_root])
    H.Me(['cml','cp -r '+pack+' '+H.pix_root+DS_root])
    os.chdir(H.pix_root+DS_root)
    H.Me(['cml','unzip -q '+pack])
    H.Me(['cml','rm -r '+pack])
    os.chdir(H.pix_root)

def MethHelp(libs):
    os_help=H.Me(['vdir',libs])
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
    import datetime, os
    # install tensorboard
#     H.Me(['cml','pip install -q tensorflow'])
    # Load the TensorBoard notebook extension
    try:
        %load_ext tensorboard
    except:
        %stop_ext tensorboard
        %reload_ext tensorboard
        
def html(content):
    """Publishes given html content into the output."""
    display.display(display.HTML(content))

def css(content=None, url=None):
    """Publishes css content."""
    if url is not None:
        html('<link rel=stylesheet type=text/css href=%r></link>' % url)
    else:
        html('<style>' + content + '</style>')
        
def javascript(content=None, url=None, script_id=None):
    """Publishes javascript content into the output."""
    if (content is None) == (url is None):
        raise ValueError('exactly one of content and url should be none')
    if url is not None:
        # Note: display.javascript will try to download script from python
        # which is very rarely useful.
        html('<script src=%r></script>' % url)
        return
    if not script_id and 'sourceURL=' not in content:
        script_id = 'js_' + hashlib.md5(content.encode('utf8')).hexdigest()[:10]

    if script_id:
        content += '\n//# sourceURL=%s' % script_id
    display.display(display.Javascript(content))
    
# set variables
H.reps_custom=['bxck75/piss-ant-pix2pix']# ,'affinelayer/pix2pix-tensorflow','phillipi/pix2pix','shelhamer/clockwork-fcn'
H.reps_all=reps
H.Me(['inst_reps',H.reps_custom,'/content/installed_reps',True,True])
H.pix_root='/content/installed_reps/piss-ant-pix2pix/'
H.gdrive_root='/content/drive/My Drive/'
H.img_input_method='raw' # dataset todo: gallery-dl scrape
H.Me(['vdir']) # show H object
