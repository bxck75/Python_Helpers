import os, sys, inspect
from pathlib import Path
import Helpers
from dlib_local import dlib
from pprint import pprint

class cli_main():

	def __init__(self):
		''' main startup class '''

		self.helpers = Helpers
		self.main_root =  self.get_project_root()
		self.colab_env = self.check_colab_env()
		# self.dynamic_helpers_lst = Helpers.__dict__ + Helpers.Core.__dict__
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
		# print(len(self.helpers_lst))

	def check_colab_env(self):
		
		try:
		  import google.colab

		  IN_COLAB = True

		except:
		  IN_COLAB = False



	def get_project_root(self) -> Path:
		"""Returns project root folder."""
		return Path(__file__).parent.parent
		cli_help = Helpers	
		cli_core = Helpers.Core
		pass

main = cli_main()
