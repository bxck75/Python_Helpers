#MoGo
os.system('apt-get install -y -qq software-properties-common python-software-properties module-init-tools')
os.system('wget https://launchpad.net/~alessandro-strada/+archive/ubuntu/google-drive-ocamlfuse-beta/+build/15331130/+files/google-drive-ocamlfuse_0.7.0-0ubuntu1_amd64.deb')
os.system('dpkg -i google-drive-ocamlfuse_0.7.0-0ubuntu1_amd64.deb')
os.system('apt-get install -f')
os.system('apt-get -y install -qq fuse')
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
os.system('google-drive-ocamlfuse -headless -id=' + creds.client_id + ' -secret=' + creds.client_secret + ' < /dev/null 2>&1 | grep URL')
vcode = getpass.getpass()
os.system('echo ' + vcode + ' | google-drive-ocamlfuse -headless -id=' + creds.client_id + ' -secret=' + creds.client_secret)
