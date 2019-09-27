#Upload Computer File into Colab
from google.colab import files
uploaded = files.upload()

#Download Computer File into Colab
files.download('saved_file.h5')
