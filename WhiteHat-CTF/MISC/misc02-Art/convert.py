from PIL import Image
import numpy as np

numpydata = np.loadtxt('misc02-Art.txt', dtype=np.uint8)
numpydata = numpydata.reshape(367,649, 3)
print(numpydata.shape)
print(numpydata)
pilImage = Image.fromarray(numpydata)
pilImage.save('flag.png')