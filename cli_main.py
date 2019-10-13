import os, sys, inspect
from pathlib import Path
import Helpers
import dlib
from pprint import pprint



class cli_main():
	def __init__(self):
		''' main startup class '''
		self.main_root =  self.get_project_root()
		self.colab_env = self.check_colab_env()	
		self.helpers_lst = [
		'ColorPrint', 'Core', 'Dlib_Face', 'FaceGrabber', 'Fileview', 'GdriveD', 'GoImgScrape', 'ICL', 
		'Img', 'RepCoList', 'ZipUp', 'core', 'dlib', 'gscrape', 'logger', 'ops', 'pprint_color', 'resize', 'DelDig', 
		'Face', 'FaceRip', 'GlobX', 'MethHelp', 'Temp', 'ViR', '_get_args', '_get_gpu', '_methods_of', '_mkd', 'cd', 
		'cdr', 'check_img_list', 'cleanup_files', 'cloner', 'combine_img_folders', 'combine_pix2pix', 'cprint', 
		'custom_reps_setup', 'cv2', 'docu', 'explore_mod', 'flickr_scrape', 'getImagesWithID', 'get_file', 
		'get_gdrive_dataset', 'get_other_reps', 'glob', 'haar_detect', 'if_exists', 'img_batch_rename', 
		'importTboard', 'install_repos', 'into_func', 'landmarkdetect', 'landmarkdetecter', 
		'landmarker', 'list_to_file', 'lrange', 'make_blank_img', 'no_action', 'np', 
		'num_files', 'os', 'path_split', 'pip', 'pix2pix', 'plt', 'rainbow', 
		'rec_walk_folder', 'resize_img', 'runProcess', 'run_pip_installer', 
		'set_maker', 'sys', 'sys_com', 'sys_log', 'valid_img', 'valid_list'
		]
		print(len(self.helpers_lst))

	def check_colab_env():
		global IN_COLAB	
		try:
		  import google.colab

		  IN_COLAB = True
		except:
		  IN_COLAB = False
		return IN_COLAB

	def get_project_root(self) -> Path:
		"""Returns project root folder."""
		return Path(__file__).parent.parent
		cli_help = Helpers	
		cli_core = Helpers.Core
		pass

m = cli_main()

pprint(Helpers.Core.__dict__)	
# ''' run pip, apt installers '''
# print('[Runnsing pip installer]')
# self.run_pip_installer()
# if 'pydrive' not in sys.modules:
# 	os.system('pip install -U -q PyDrive')
# 	''' PyDrive install '''
# 	print('[Installing PyDrive]')
# 	sr = self.sys_com('python ' + self.git_install_root + '/PyDrive/setup.py install')

# if 'icrawler' not in sys.modules:
# 	os.system('pip install icrawler')


# ''' needed googledrive repos '''
# gdrive_rps=[
#     'bxck75/google-drive-list-shared', 
#     'bxck75/PyDrive'
# ]
# Helpers.Core().install_repos(gdrive_rps, inst_dir, False, True)


# import pydrive
# ''' google shared wrapper '''
# print('[Installing google wrapper]')
# sr += Helpers.Core().sys_com('cp ' + self.git_install_root + '/google-drive-list-shared/google-drive-list-shared.py ' +  self.core_dirname + '/gdrive_shared.py')
# sr += Helpers.Core().sys_com('rm -r ' + self.git_install_root + '/google-drive-list-shared')
# print(sr)

# pprint(str(str(dir(dlib)).split('face')[0]))



# class cli_local_run:
# 	''' class for use when opperating from cli '''
# 	def __init__(self):
# 		print('Init ' + __name__)

# class main:
#     ''' This and the core.py file are the main frontier of development '''
#     def __init__(self):
#         ''' set root paths '''
#         print('init ' + __name__ )
