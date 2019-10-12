# a list of repos for machinelearning
reps=[
        'bxck75/TowardsDataScience',
        'bxck75/perceptron-benchmark',
        'bxck75/Facial-Landmark-Detector',
        'CMU-Perceptual-Computing-Lab/openpose',
        'mrgloom/Face-landmarks-detection-benchmark',
        'bxck75/openface',
        'bxck75/ipyleaflet',
        'bxck75/face-recognition',
        'bxck75/dosage',
        'bxck75/opencv',
        'bxck75/opencv_contrib',
        'bxck75/Face_Zoo',
        'googlecreativelab/quickdraw-dataset',
        'divamgupta/ladder_network_keras',
        'zhixuhao/unet',
        'yihui-he/u-net',
        'alina1021/facial_expression_transfer',
        'shekkizh/FCN',
        'sadeepj/crfasrnn_keras',
        'fastai/fastai',
        'drallensmith/neat-python',
        'CodeReclaimers/neat-python',
        'uber-research/deep-neuroevolution',
        'MorvanZhou/Evolutionary-Algorithm',
        'llSourcell/blockchain-python-tutorial',
        'llSourcell/autoencoder_demo',
        'llSourcell/autoencoder_explained',
        'llSourcell/awesome-public-datasets',
        'llSourcell/7_Research_Directions_Deep_Learning',
        'hardmaru/sketch-rnn',
        'hardmaru/sketch-rnn-datasets',
        'hardmaru/sketch-rnn-poste',
        'Gogul09/virtual-drum',
        'ytdl-org/youtube-dl',
        'nnUyi/GAN-Collections',
        'mikf/gallery-dl',
        'corenel/Realistic-Neural-Talking-Head-Models',
        'bxck75/piss-ant-pix2pix',
        'bxck75/datasets',
        'hardmaru/estool',
        'deepmipt/DeepPavlov',
        'bxck75/A1_Colabs',
        'tjwei/Flappy-Turtle.',
        'tjwei/fonttools',
        'tjwei/blender3d_import_psk_psa',
        'lllyasviel/sketchKeras',
        'Mckinsey666/Anime-Face-Dataset',
        'chenyuntc/pytorch-book',
        'lllyasviel/style2paints',
        'llSourcell/GANS-for-style-transfer',
        'opencv/open_model_zoo',
        'hindupuravinash/the-gan-zoo',
        'corenel/GAN-Zoo',
        'eriklindernoren/Keras-GAN',
        'junyanz/CycleGAN',
        'junyanz/pytorch-CycleGAN-and-pix2pix',
        'junyanz/iGAN',
        'martinarjovsky/WassersteinGAN',
        'shaoanlu/faceswap-GAN',
        'LantaoYu/SeqGAN',
        'tjwei/GANotebooks',
        'adeshpande3/Tensorflow-Programs-and-Tutorials',
        'adeshpande3/Generative-Adversarial-Networks',
        'adeshpande3/KaggleGhosts',
        'adeshpande3/OpenAI_Gym_Universe',
        'diegoalejogm/gans',
        'osh/KerasGAN',
        'r9y9/gantts',
        'jayleicn/animeGAN',
        'jayleicn/ImageNet-Training',
        'Zardinality/WGAN-tensorflow',
        'RossMcKenzie/TreeGAN',
        'martinarjovsky/WassersteinGAN',
        'timsainb/Tensorflow-MultiGPU-VAE-GAN',
        'Larox/python-moviepy-meetup',
        'tjwei/keras-yolo3',
        'tensorflow/gan',
        'tensorflow/moonlight'
        'tensorflow/models',
        'tensorflow/datasets',
        'tensorflow/docs',
        'mnicnc404/CartoonGan-tensorflow',
        'Yijunmaverick/CartoonGAN-Test-Pytorch-Torch',
        'keras-team/keras-contrib',
        'mnicnc404/CartoonGan-tensorflow',
]

repos_sorted = sorted(reps)
matchers = ['bxck75']
bxck75_repos = [s for s in repos_sorted if any(xs in s for xs in matchers)]
bxck75_repos.sort()
