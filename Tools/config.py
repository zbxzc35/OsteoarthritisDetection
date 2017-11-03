# Config file

#############################
# DATASET settings
#############################

datasetRoot = '/home/ggutierrez/Test/dataset'

#############################
# FEATURE extraction settings
#############################

# HOG parameters

orientations = 8
pixel_per_cell = (16, 16)
cell_per_block = (1, 1)
block_norm = 'L2-Hys'
#normalise = True

# Downscale factor for the pyramid

downScaleFactor = 2

# Location to store the features

inputFoldePath = '/home/ggutierrez/Test/input'
outputFolderPath = '/home/ggutierrez/Test/output'
