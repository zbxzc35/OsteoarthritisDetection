from skimage import io, data
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
from Tools import config as cfg
from PIL import Image

img = Image.open(cfg.imagePath)
image = io.imread(cfg.imagePath)
#image = data.astronaut()
fig, (ax1) = plt.subplots(1)
ax1.set_title('Random Patches Sampling')
ax1.imshow(img)
ax1.axis('off')

y,x = image.shape[0:2]
print("Image size:", x, y)

num_of_patches = cfg.num_of_patches
(patch_width, patch_height) = cfg.patch_shape

# Sample radius
sample_radius = 20

# Random values for X and Y
#x_values = [random.randint(10, x) for p in range(0,num_of_patches)]
#y_values = [random.randint(10, y) for p in range(0,num_of_patches)]
x_values = [random.randint(30,250) for p in range(0,num_of_patches)]
y_values = [random.randint(320,500) for p in range(0,num_of_patches)]

print(x_values)
print(y_values)

for i in range(num_of_patches):
    x_pos = x_values[i]
    y_pos = y_values[i]
    patch = patches.Rectangle((x_pos,y_pos),patch_width,patch_height,linewidth=1,edgecolor='g',facecolor='none')
    ax1.add_patch(patch)

print('Last Position:',x_pos, y_pos)

area = (x_pos, y_pos, x_pos+100, y_pos+100)
cropped_img = img.crop(area)

parche = image[y_pos:y_pos+100, x_pos:x_pos+100]

#ax2.set_title('Patch')
#ax2.imshow(cropped_img)
#fig.savefig('img.png', dpi=90, bbox_inches='tight')
plt.show()