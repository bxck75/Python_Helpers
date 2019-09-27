#Big Helpers Loading
from pathlib import Path
import os, inspect
try:
    os.system('rm -r /content/sample_data')
    os.system('rm -r /content/ProjectPrimer.py')
except:
    print('No default garbage to remove')
os.system('mkdir -p /content/lib')
lib_file=Path('/content/lib/Helpers.py')
if not lib_file.is_file():
    os.chdir('/content/lib')
    os.system('wget https://raw.githubusercontent.com/bxck75/PyHelpers/master/BigHelp.py -O /content/lib/BigHelp.py')
os.chdir('/content/')
# import the biggest help
from lib.BigHelp import Helpers
# installing done......bring in the helpers!
global H
H=Helpers()
# bring in the helpers!
H.Me(['cml','echo "Pull in the helpers!"'])
H.prime=['bxck75/PyHelpers']
H.Me(['inst_reps',H.prime,'/content/lib',True,True])
H.Me(['cml','echo "All Done!"'])
# os.chdir('/content/')
os.system('rm -r /content/lib/BigHelp.py')
