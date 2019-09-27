# Usage : ZipDown.py 'id' 'target/folder' 'filename'
import os, zipfile, sys
os.system('pip install -U -q PyDrive')

# Insert your file ID
# Get it by generating a share URL for the file
zip_file = sys.argv[1]
zip_id = '1zppBj6lZFMdDprLmdCDedULrHQG4E9iM'

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# 1. Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

# 2. Download Zip
print ("Downloading zip file")
myzip = drive.CreateFile({'id': zip_id})
myzip.GetContentFile(sys.argv[3])

# 3. Unzip
print ("Uncompressing zip file")
zip_ref = zipfile.ZipFile('model.zip', 'r')
zip_ref.extractall(sys.argv[2]+'/')
zip_ref.close()
