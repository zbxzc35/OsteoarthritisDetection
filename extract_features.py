import os
import pickle

from skimage import io, util, color
from Tools import config as cfg, feature_extractor

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


def extractAndStoreFeaturesForPatches(imagesList):
    print('Extracting features...')
    matrixOfFeatsPerImage = list()

    for img in imagesList:
        print('Processing Image')
        featsList = list()
        for patch in img:
            print('Extracting features of patch ... from image ...')
            #image = io.imread(patch, as_grey=True)
            image = color.rgb2grey(patch)
            image = util.img_as_uint(image)
            feats = feature_extractor.extractHOGFeatures(image)
            featsList.append(feats)
        matrixOfFeatsPerImage.append(featsList)

    return matrixOfFeatsPerImage


if __name__ == '__main__':
    run()