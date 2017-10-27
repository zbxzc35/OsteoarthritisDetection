
from skimage.feature import hog

from Tools import config as cfg


def extractHOGFeatures(image):
    feats = hog(image,
                orientations=cfg.orientations,
                pixels_per_cell=cfg.pixel_per_cell,
                cells_per_block=cfg.cell_per_block,
                block_norm=cfg.block_norm,
                visualise=False,
                normalise=cfg.normalise)
    return feats
