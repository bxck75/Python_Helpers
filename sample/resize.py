def resize(folder):
    '''
        # Example resize('/root/Bureaublad/data/boefjes/front')
    '''
    from PIL import Image
    import os,sys,glob
    for root, dirs, files in os.walk(folder, topdown=False):
        print('[Resizing '+str(len(files))+' files]')
        for name in files:
            print(os.path.join(root, name))
            im = Image.open(os.path.join(root, name))
            rgb_im = im.convert('RGB')
            name, ext = name.split('.'):
            outfilename = '/'+name+'%d.'+ext % int(i + 1)
            outfile=os.path.join(directory, outfilename)
            print(directory+outfile)
            rgb_im.save(directory+outfile)

                
