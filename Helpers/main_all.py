import tensorflow as tf
import os
from .BEGAN import *
from .DCGAN import *



flags = tf.app.flags
flags.DEFINE_bool("is_training", False, "training flag")
flags.DEFINE_string("gan", 'BEGAN', "training flag")
FLAGS = flags.FLAGS

def check_dir():
    if not os.path.exists('./sample'):
        os.mkdir('./sample')
    if not os.path.exists('./checkpoint'):
        os.mkdir('./checkpoint')
    if not os.path.exists('./logs'):
        os.mkdir('./logs')

def main():
    check_dir()
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.33)
    config = tf.ConfigProto(gpu_options=gpu_options)
    config.gpu_options.allow_growth=True
    with tf.Session(config=config) as sess:
        if FLAGS.gan:
            gan = FLAGS.gan(input_height=64, input_width=64, input_channels=3, output_height=64, output_width=64, gf_dim=64, input_fname_pattern = '*.jpg', is_grayscale=False, sess = sess)
            gan.build_model()
        
        if FLAGS.is_training:
            gan.train()
            
#         gan = BEGAN(input_height=64, input_width=64, input_channels=3, output_height=64, output_width=64, gf_dim=64, input_fname_pattern = '*.jpg', is_grayscale=False, sess = sess)
#         gan.build_model()
    
if __name__=='__main__':
    main()
