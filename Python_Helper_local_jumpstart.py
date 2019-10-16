import os, sys, inspect
from pathlib import Path

root = '/content'
helpers_path = root + '/installed_repos/Python_Helpers'
os.makedirs(helpers_path , exist_ok=True)
os.system('sudo rm -r ' + helpers_path) # clear for new pull from git
os.system('git clone https://github.com/bxck75/Python_Helpers.git '+helpers_path) # git clone the helpers
os.chdir(helpers_path)
os.system('python setup.py install')
os.system('python cli_main.py')
