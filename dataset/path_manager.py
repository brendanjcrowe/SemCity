import os

# manual definition
PROJECT_NAMES = 'SemCity' 
SEMKITTI_DATA_PATH = 'dataset/dataset/sequences' # the path to the sequences folder
CARLA_DATA_PATH = '' # the path to the sequences folder
# '/home/xujia/dataset/KITTI/dataset/sequences'
# auto definition
CARLA_YAML_PATH = os.getcwd() + '/dataset/carla.yaml'
SEMKITTI_YAML_PATH = os.getcwd() + '/dataset/semantic-kitti.yaml'

# manual definition after training
AE_PATH = os.getcwd() + ''  # the path to the pt file 
# GEN_DIFF_PATH = os.getcwd() + '' 
GEN_DIFF_PATH = "exp/diff/ema_0.9999_050000.pt"
SSC_DIFF_PATH = os.getcwd()  + ''