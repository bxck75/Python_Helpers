Sample Module Repository
========================

This simple project is an example repo for Python projects.

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.
Colab starter :
'''
# remove defaults
!rm -r sample_data
# Clone the frame
!git clone https://github.com/bxck75/Python_Helpers.git
# Change dir
%cd /content/Python_Helpers
# install
!python setup.py install
import main
'''
