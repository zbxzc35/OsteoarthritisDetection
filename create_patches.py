from Tools import config as cfg
from skimage import io
import random, os
import numpy as np

def run():
    datasetImages = os.listdir(cfg.datasetRoot)
    datasetImages = filter(lambda element: '.png' in element, datasetImages)

    # Lists
    patches_per_image = []
    patch_centres_per_image = []

    for filename in datasetImages:
        imagePath = cfg.datasetRoot + '/' + filename
        image = io.imread(imagePath)
        patches, patchCentres = createPatchesRandomly(image)
        patches_per_image.append(patches)
        patch_centres_per_image.append(patchCentres)

    # Convert list to ndarrays
    #patches_per_image = np.array(patches_per_image,ndmin=5)
    patch_centres_per_image = np.array(patch_centres_per_image)

    return patches_per_image, patch_centres_per_image



def createPatchesRandomly(image):
    (patch_width, patch_height) = cfg.patch_shape
    num_of_patches = cfg.num_of_patches
    sample_radius = 50

    # Generate int values randomly
    x_values = [random.randint(30, 250) for p in range(0, num_of_patches)]
    y_values = [random.randint(320, 500) for p in range(0, num_of_patches)]

    # Lists
    patches = []
    patch_centres = []

    for i in range(num_of_patches):
        x_pos = x_values[i]
        y_pos = y_values[i]
        # Calculate the patch centres
        cx_patch = x_pos + (patch_width//2)
        cy_patch = y_pos + (patch_height//2)
        patch_centres.append([cx_patch, cy_patch])
        # Extract the patch
        patch = image[y_pos:y_pos+patch_height, x_pos:x_pos+patch_width]
        patches.append(patch)

    #Convert lists to ndarrays
    patches = np.array(patches)
    patch_centres = np.array(patch_centres) # (5,2)

    return patches, patch_centres

if __name__ == '__main__':
    run()