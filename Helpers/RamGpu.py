def RGPU():
  # memory footprint support libraries/code
  H.Me(['cml','ln -sf /opt/bin/nvidia-smi /usr/bin/nvidia-smi'])
  H.Me(['cml','pip install gputil'])
  H.Me(['cml','pip install psutil'])
  H.Me(['cml','pip install humanize'])
  import psutil
  import humanize
  import os
  import GPUtil as GPU
  GPUs = GPU.getGPUs()
  gpu = GPUs[0]
  def printm():
    process = psutil.Process(os.getpid())
    print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " I Proc size: " + humanize.naturalsize( process.memory_info().rss))
    print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
  printm()
