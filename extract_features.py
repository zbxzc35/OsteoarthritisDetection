import os
import pickle
from skimage import io, util, color
from Tools import config as cfg, feature_extractor
import numpy as np

inputPath = cfg.inputFoldePath
outputPath = cfg.outputFolderPath


def run():
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)

    print('Extracting features from ' + inputPath + ' in ' + outputPath)

    extractAndStoreFeatures(inputPath, outputPath)


def extractAndStoreFeatures(inputFolder, outputFolder):
    fileList = os.listdir(inputFolder)
    imagesList = filter(lambda element: '.png' in element, fileList)

    for filename in imagesList:
        imagePath = inputFolder + '/' + filename
        outputPath = outputFolder + '/' + filename + '.feat'

        print('Extracting features for ' + imagePath)

        image = io.imread(imagePath, as_grey=True)
        image = util.img_as_uint(image)
        feats = feature_extractor.extractHOGFeatures(image)

        outputFile = open(outputPath, 'wb')
        pickle.dump(feats, outputFile)
        outputFile.close()


def extractFeaturesForPatches(images):
    print('Extracting features...')
    featsPerImage = []

    for img in images:
        print('Processing Image')
        features = []
        for patch in img:
            print('Extracting features of patch ... from image ...')
            #image = io.imread(patch, as_grey=True)
            image = color.rgb2grey(patch)
            image = util.img_as_uint(image) # doubt #
            feats = feature_extractor.extractHOGFeatures(image)
            features.append(feats)
        featsPerImage.append(features)

    # Convert list to ndarray
    featsPerImage = np.array(featsPerImage)

    return featsPerImage


if __name__ == '__main__':
    run()