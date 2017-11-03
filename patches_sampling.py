from skimage import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

image = io.imread('/home/ggutierrez/H5RXfinal.png')
fig, ax = plt.subplots(1)
ax.imshow(image)
y,x = image.shape[0:2]
print(x)
print(y)
#print(len(image))

num_of_patches = 20

# Random values for X and Y
x_values = [random.randint(10,x-100) for p in range(0,num_of_patches)]
y_values = [random.randint(10,y-100) for p in range(0,num_of_patches)]

print(x_values)
print(y_values)

for i in range(num_of_patches):
    x_pos = x_values[i]
    y_pos = y_values[i]
    patch = patches.Rectangle((x_pos,y_pos),40,40,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(patch)

#fig.savefig('img.png', dpi=90, bbox_inches='tight')
plt.show()