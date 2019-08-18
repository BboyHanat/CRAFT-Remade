"""
Config containing all hardcoded parameters for training weak supervised model on datasets like icdar 2013
"""

seed = 0

use_cuda = True
num_cuda = "0"

save_path = '/home/SharedData/Mayank/Models/WeakSupervision/ICDAR2013'

images_path = '/home/SharedData/Mayank/ICDAR2013/Images'
target_path = '/home/SharedData/Mayank/ICDAR2013/Generated'

prob_synth = 0

DataLoaderSYNTH_base_path = '/home/SharedData/Mayank/SynthText/Images'
DataLoaderSYNTH_mat = '/home/SharedData/Mayank/SynthText/gt.mat'
DataLoaderSYNTH_Train_Synthesis = '/home/SharedData/Mayank/Models/SYNTH/train_synthesis/'

DataLoaderICDAR2013_Synthesis = '/home/SharedData/Mayank/ICDAR2013/Save/'

ICDAR2013_path = '/home/SharedData/Mayank/ICDAR2013'

batch_size = {
	'train': 3,
	'test': 3,
}

lr = {
	1: 1e-4,
	4000: 1e-5,
	8000: 1e-6,
}

threshold_character = 0.4
threshold_affinity = 0.4
threshold_fscore = 0.5

iterations = batch_size['train']*10000
