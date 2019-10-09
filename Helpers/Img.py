class Tools:
  ''' 
  Tools for images and video
    Example:
      resize_single(img_path pad=False, size=400)
      resize_folder('/root/Bureaublad/data/boefjes/front')
  '''
  import matplotlib.pyplot as plt
  import numpy as np
  import cv2
  
  def ShowImg(path, fig_id, clone=False):
      ''' 
      Show image
              ShowImg(<img path>, <id>)
          Example: 
              ShowImg('/content/images_google/000006.jpg', 1)
              ShowImg('/content/images_google/000004.jpg', 2)  
      '''
      import cv2
      from numpy import random
      import matplotlib.pyplot as plt 

      img = cv2.imread(path)
      img_rainbow = cv2.cvtColor(img, cv2.COLORMAP_RAINBOW)
      plt.figure(figsize = (10,20))
      plt.axis('off')
      
#       font = cv2.FONT_HERSHEY_SIMPLEX
#       text = cv2.putText(img_rainbow,'K00B404',(10,45), font, 2,(2,1,112), 4, cv2.LINE_AA)
#       plt.imshow(text)

      plt.imshow(img_rainbow)
      # imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, 
          # extent=None, shape=None, filternorm=1, filterrad=4.0, imlim=None, resample=None, url=None, *, data=None, **kwargs)
      plt.show
      if clone:
          # img save clone in _cloned folder
          cv2.imwrite(path.replace('images','images_cloned'),img)


  def make_image(data, outputname, size=(1, 1), dpi=80):
      ''' make_image(data, '/tmp/out.png', size=(1, 1), dpi=80) '''
      fig = plt.figure()
      fig.set_size_inches(size)
      ax = plt.Axes(fig, [0., 0., 1., 1.])
      ax.set_axis_off()
      fig.add_axes(ax)
      plt.set_cmap('hot')
      ax.imshow(data, aspect='equal')
      plt.savefig(outputname, dpi=dpi)
      ''' ####################### '''
#       data = mpimg.imread(inputname)[:,:,0]
#       data = np.arange(1,10).reshape((3, 3))
#       make_image(data, '/tmp/out.png')
  
  
  def help(self,input,output):
    ''' help '''
    print(self)
    dir(self)
    help(self)
