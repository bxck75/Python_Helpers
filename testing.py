from cli_main import *

this_env = str(os.environ).replace('[','').replace(']','').split(',')
# this_env.sort()
pprint(this_env)
pprint(dir(main.high_core))

# import os
# os.environ['DEBUSSY'] = '1'
# os.environ['FSDB'] = '1'
# # Open child processes via os.system(), popen() or fork() and execv()
# someVariable = int(os.environ['DEBUSSY'])

# core.get_detector_stuff(core) 

# print(detect_model_locs)
''' ############################################################################################ '''
# core.pix2pix(self, dataset_path, images_set_name, epochs=2, loops=2, mode='train', first_run=True)
''' ############################################################################################ '''


# print(dir(main))
# print(main.main_root)
# print(main.get_project_root())