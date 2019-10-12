import os, sys, inspect
os.system('git clone https://github.com/bxck75/Python_Helpers.git')
os.chdir('Python_Helpers')
os.system('python setup.py install')
from pathlib import Path
import Helpers

print(os.environ)
print(locals)
print(globals)
os.system('pip install icrawler')

class cli_local_run:
	''' class for use when opperating from cli '''
	def __init__(self):
		print('Init ' + __name__)

class main:
    ''' This and the core.py file are the main frontier of development '''
    def __init__(self):
        ''' set root paths '''
        print('init ' + __name__ )
