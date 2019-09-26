# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample

# print(sys.path)
# help()
# help(sample.helpers)
# print(dir(sample))
# sample.hmm('ZipUp')
# sample.hmm()
# print(sample.ZipUp.__dict__['__file__'])
# print(dir(sample.ZipUp))
# print(dir(sample.BigHelp))
# print(dir(sample.RepCoList.reps))
# print(dir(sample.custom_functions))
H=sample.BigHelp.Helpers()
H.zipper=sample.ZipUp
zipname='Samplemod2'
foldername='/content/drive/My\ Drive'
target_dir='/content/samplemod'
print(H.Me(['vdir',[H.zipper]]))
item_to = H.zipper.ZipUp(zipname, foldername, target_dir)
print(item_to.ZipUp)