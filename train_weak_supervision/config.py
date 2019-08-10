use_cuda = True
num_cuda = "0,3"

save_path = '/home/SharedData/Mayank/Models/WeakSupervision/ICDAR2013'

images_path = '/home/SharedData/Mayank/ICDAR2013/ch2_training_images'
target_path = '/home/SharedData/Mayank/ICDAR2013/Generated'

prob_synth = 0.2

DataLoaderSYNTH_base_path = '/home/SharedData/Mayank/SynthText/Images'
DataLoaderSYNTH_mat = '/home/SharedData/Mayank/SynthText/gt.mat'
DataLoaderSYNTH_Train_Synthesis = '/home/SharedData/Mayank/Models/SYNTH/train_synthesis/'

DataLoaderICDAR2013_Synthesis = '/home/SharedData/Mayank/ICDAR2013/Save/s'

ICDAR2013_path = '/home/SharedData/Mayank/ICDAR2013'

batch_size = {
	'train': 6,
	'test': 3,
}

lr = {
	1: 5e-5,
	10000: 2.5e-5,
	20000: 1e-5,
	40000: 5e-6,
	60000: 1e-6,
}

periodic_fscore = 100
periodic_output = 1000
periodic_save = 10000

threshold_character = 0.4
threshold_affinity = 0.4
threshold_fscore = 0.5
threshold_first_character = 0.5
threshold_boundary = 0.5

iterations = 1000
