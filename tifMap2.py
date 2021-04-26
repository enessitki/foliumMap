from matplotlib import pyplot as plt
from osgeo import gdal
import matplotlib.pyplot as plot
import numpy as np

dataset = gdal.Open(r'g_i33a1.tiff')
band1 = dataset.GetRasterBand(1) # Red channel
band2 = dataset.GetRasterBand(2) # Green channel
band3 = dataset.GetRasterBand(3)

b1 = band1.ReadAsArray()
b2 = band2.ReadAsArray()
b3 = band3.ReadAsArray()
img = np.dstack((b1, b2, b3))


f = plt.figure()
plt.imshow(img)
plt.savefig('result.png')
plt.show()