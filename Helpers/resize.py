import cv2
def resize_folder(folder):
    '''
        # Example resize('/root/Bureaublad/data/boefjes/front')
    '''
    from PIL import Image
    import os,sys,glob,cv2
    for root, dirs, files in os.walk(folder, topdown=False):
        print('[Resizing '+str(len(files))+' files]')
        i=0
        for name in files:
            print(os.path.join(root, name))
            im = Image.open(os.path.join(root, name))
            rgb_im = im.convert('RGB')
            name, ext = name.split('.')
            outfilename = '/'+name+'%d.'+ext % int(i + 1)
            outfile=os.path.join(directory, outfilename)
            print(directory+outfile)
            rgb_im.save(directory+outfile)
            i+=1
            
def resize_single(src,pad=False,size=256):
    '''
        resize(img,pad,size)
    '''
    import cv2
    imag = cv2.imread(src)
    height, width, _ = imag.shape
    dst = imag
    if height != width:
        if pad:
            size = max(height, width)
            # pad to correct ratio
            oh = (size - height) // 2
            ow = (size - width) // 2
            dst = imag.pad(image=dst, offset_height=oh, offset_width=ow, target_height=size, target_width=size)
        else:
            # crop to correct ratio
            size = min(height, width)
            oh = (height - size) // 2
            ow = (width - size) // 2
            dst = imag.crop(image=dst, offset_height=oh, offset_width=ow, target_height=size, target_width=size)

    assert(dst.shape[0] == dst.shape[1])

    size, _, _ = dst.shape
    if size > size:
        dst = imag.downscale(images=dst, size=[size, size])
    elif size < size:
        dst = imag.upscale(images=dst, size=[size, size])
    return dst 
