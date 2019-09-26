import os
os.system('pip install -U -q PyDrive')
from google.colab import files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
import zipfile
import os
import sys

class ZipUp:

    def __init__(self, zipname, foldername, target_dir):
        ''' init the details for the zip and push'''
        self.zipname = zipname
        self.foldername = foldername
        self.target_dir = target_dir

    @property
    def ZipUp(self):
        ''' define the zip_n_push property'''
        if( self.zipname !='' and self.foldername != '' and self.target_dir != '' ):
            self.zipfolder()
            self.g_login()
            self.make_push()
            self.status = self.status + self.get_id()
            return self.status
        
    def zipfolder(self):
        ''' zip the selected folder to the target dir with '''
        zipobj = zipfile.ZipFile(self.zipname + '.zip', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(self.target_dir) + 1
        for base, dirs, files in os.walk(self.target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
        self.status='zipped '
                
    def g_login(self):
        ''' Authenticate and create the PyDrive client.'''
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        self.drive = GoogleDrive(gauth)
        self.status= self.status+'and '
        
    def make_push(self):
        ''' Create & upload a file text file.'''
        file1 = self.drive.CreateFile({'id':self.get_id()})
        file1.SetContentFile(self.zipname+".zip")
        file1.Upload()
        self.status= self.status+'pushed! (id) '

    def get_id(self):
        query = "title = '"+self.zipname+".zip'"
        file_list = self.drive.ListFile({'q': query}).GetList()
        for file in file_list:
            if file['labels']['trashed'] ==False:
                return file['id']

if __name__ == "__main__":
    item_to = ZipUp('sample_data','/content/drive/My Drive','/content/lib/PyHelpers')
    print(item_to.ZipUp)