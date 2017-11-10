from Tools import config as cfg
from skimage import io
import random, os


def run():
    datasetImages = os.listdir(cfg.datasetRoot)
    datasetImages = filter(lambda element: '.png' in element, datasetImages)

    patches_per_image_list = list()
    centres_patches_per_image_list = list()
    for filename in datasetImages:
        imagePath = cfg.datasetRoot + '/' + filename
        image = io.imread(imagePath)
        patchesList, patchCentresList = createPatchesRandomly(image)
        patches_per_image_list.append(patchesList)
        centres_patches_per_image_list.append(patchCentresList)

    #print(type(patches_per_image_list))
    #print(patches_per_image_list)
    return patches_per_image_list, centres_patches_per_image_list



def createPatchesRandomly(image):
    (patch_width, patch_height) = cfg.patch_shape
    num_of_patches = cfg.num_of_patches
    sample_radius = 50

    x_values = [random.randint(30, 250) for p in range(0, num_of_patches)]
    y_values = [random.randint(320, 500) for p in range(0, num_of_patches)]

    patchesList = list()
    patch_centres = list()

    for i in range(num_of_patches):
        x_pos = x_values[i]
        y_pos = y_values[i]
        cx_patch = x_pos + (patch_width//2)
        cy_patch = y_pos + (patch_height//2)
        patch_centres.append([cx_patch, cy_patch])

        patch = image[y_pos:y_pos+patch_height, x_pos:x_pos+patch_width]
        patchesList.append(patch)

    return patchesList, patch_centres

if __name__ == '__main__':
    run()