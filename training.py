from Tools import config as cfg
#import patches_sampling
import create_patches, extract_features
import os

def run():
    # List of X-Ray images in PNG format
    imagesList = os.listdir(cfg.datasetRoot)
    imagesList = filter(lambda element: '.png' in element, imagesList)
    count = len(list(imagesList))

    print('Training the system with', count,'X-Ray Images...')

    # create patches (retornar los centros de los parches tambien)
    patchesList, patchesCentresList = create_patches.run()

    # extract features
    matrixOfFeatures = extract_features.extractAndStoreFeaturesForPatches(patchesList)
    matrixOfCentres = patchesCentresList

    print('Features Matrix:', matrixOfFeatures.__len__())
    print('Patch Centres Matrix:', matrixOfCentres.__len__())

if __name__ == '__main__':
    run()