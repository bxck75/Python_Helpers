import os, sys, inspect
from pathlib import Path
import Helpers
from dlib_local import dlib
from pprint import pprint

''' main startup class '''
class cli_main():
	''' init of the low and high helper Cores '''
	def __init__(self):

		def check_colab_env():
			'''check on google.colab'''
			try:
			  import google.colab
			  return True
			except:
			  return False

		def get_project_root() -> Path:
			''' Returns project root folder.'''
			return Path(__file__).parent.parent

		''' check if the env is colaboratory '''
		self.colab_env = check_colab_env()
		''' get the underlaying project root '''
		self.main_root =  str(get_project_root())

		def del_install_check():
			try:
				if sys.argv[1] == 'new':
					print(self.main_root  + '/install.check')
					os.remove(self.main_root + '/Python_Helpers/Helpers/install.check')
			except:
				print(self.main_root  + '/Python_Helpers/Helpers/install.check')
				pass


		''' see if install is needed '''
		del_install_check()

		''' Set core tools name '''
		self.high_core = Helpers
		''' init the core '''
		self.high_core.Core() ######init#####
		''' set default tools name '''
		self.low_core = Helpers.Core
		# print(self.high_core.__name__ )
		# print(self.low_core.__name__)

		def meth_lister(key):
			''' method lister '''
			m_list = {
					self.high_core.__name__ :dir(self.high_core), # few system methods in core
					self.low_core.__name__ :dir(self.low_core), # bulk of methods in Core
					}
			if key == 'all':
				return m_list
			else:
				m_res=m_list[key]
				return m_res


		# Helpers.get_detector_stuff(self.high_core)


		''' Dynamic method listing '''
		self.low_core.meth_lst = meth_lister('Helpers')
		self.high_core.meth_lst = meth_lister('Core')
		self.lst_of_methods = meth_lister('all')
		# pprint(self.lst_of_methods)

main = cli_main()


# {'Core': ['DelDig', 'Face', 'FaceRip', 'GlobX', 'MethHelp', 'Temp', 'ViR', 'Zip', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_args', '_get_gpu', '_methods_of', '_mkd', 'cd', 'cdr', 'check_img_list', 'cleanup_files', 'cloner', 'combine_img_folders', 'combine_pix2pix', 'cprint', 'custom_reps_setup', 'cv2', 'detect_cat_faces', 'docu', 'explore_mod', 'flickr_scrape', 'getImagesWithID', 'get_file', 'get_gdrive_dataset', 'get_other_reps', 'glob', 'haar_detect', 'if_exists', 'img_batch_rename', 'importTboard', 'install_repos', 'into_func', 'landmarkdetect', 'landmarkdetecter', 'landmarker', 'list_to_file', 'lrange', 'make_blank_img', 'meth_lst', 'np', 'num_files', 'os', 'path_split', 'pip', 'pix2pix', 'plt', 'rainbow', 'rec_walk_folder', 'resize_img', 'runProcess', 'run_pip_installer', 'set_maker', 'sys', 'sys_com', 'sys_log', 'valid_img', 'valid_list'], 'Helpers': ['ColorPrint', 'Core', 'Dlib_Face', 'FaceGrabber', 'Fileview', 'GdriveD', 'GoImgScrape', 'ICL', 'Img', 'RepCoList', 'ZipUp', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'core', 'detect_squares', 'get_detector_stuff', 'gscrape', 'logger', 'meth_lst', 'ops', 'pprint_color', 'resize']}