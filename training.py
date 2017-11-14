from Tools import config as cfg
#import patches_sampling
import create_patches, extract_features
import os
import numpy as np

def run():
    # List of X-Ray images in PNG format
    imagesList = os.listdir(cfg.datasetRoot)
    imagesList = filter(lambda element: '.png' in element, imagesList)
    count = len(list(imagesList))

    print('Training the system with', count,'X-Ray Images...')

    # Extract Patches and Patch Centres of all X-Ray Images
    patchesPerImage, patchCentresPerImage = create_patches.run()

    # Feature Vector Matrix
    matrixOfFeatures = extract_features.extractFeaturesForPatches(patchesPerImage)
    # Patch Centres Matrix
    matrixOfCentres = patchCentresPerImage

    print(type(matrixOfFeatures))
    print(type(matrixOfCentres))


if __name__ == '__main__':
    run()