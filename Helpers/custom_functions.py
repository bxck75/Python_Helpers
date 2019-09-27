'''Own functions list'''
def get_gdrive_dataset(pack, DS_root='datasets',GD_root='datasets'):
    import google
    from google.colab import drive
    drive.mount('/content/drive', force_remount=True)
    H.GD_ROOT=GD_root+'/'
    H.DS_ROOT=DS_root+'/'
    os.chdir(H.gdrive_root+H.GD_ROOT)
    H.Me(['mkd',[DS_root,'models'],H.pix_root])
    H.Me(['cml','cp -r '+pack+' '+H.pix_root+DS_root])
    os.chdir(H.pix_root+DS_root)
    H.Me(['cml','unzip -q '+pack])
    H.Me(['cml','rm -r '+pack])
    os.chdir(H.pix_root)

def MethHelp(libs):
    os_help=H.Me(['vdir',libs])
    #make a list containing libs values of os_help
    listOfLibs = [x[0] for x in os_help]
    #make a list containing libs method values of os_help
    listOfMethods= [x[1] for x in os_help]
    # Create a zipped list of tuples from above lists
    zippedList =  list(zip(listOfLibs, listOfMethods[0:5]))
    zippedList
    # request help on method from list
    return zippedList
    
def loadTboard():
    '''load tensorboard'''
    import datetime, os ,tensorboard
    # install tensorboard
    #     H.Me(['cml','pip install -q tensorflow'])
    # Load the TensorBoard notebook extension
#     try:
#         %load_ext tensorboard
#     except:
#         %reload_ext tensorboard