# from matplotlib import pyplot as plt
# from matplotlib import cm
#
# from PIL import Image
# from numpy import array
#
# im = Image.open('g_i33a1.tiff')
# im.show()


# import matplotlib.pyplot as plt
# I = plt.imread('g_i33a1.tiff')

# import cv2
# image = cv2.imread('g_i33a1.tiff')
# cv2.imshow('tif image',image)

# from PIL import Image
# import numpy
#
# im = Image.open('g_i33a1.tiff')
# imarray = numpy.array(im)
# imarray.shape
# im.show()

import numpy as np
import struct
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
from osgeo import gdal_array
from osgeo.gdalconst import *
import matplotlib.pyplot as plt

cube = gdal.Open('g_i33a1.tiff')
bnd1 = cube.GetRasterBand(29)
bnd2 = cube.GetRasterBand(19)
bnd3 = cube.GetRasterBand(9)

img1 = bnd1.ReadAsArray(0,0,cube.RasterXSize, cube.RasterYSize)
img2 = bnd2.ReadAsArray(0,0,cube.RasterXSize, cube.RasterYSize)
img3 = bnd3.ReadAsArray(0,0,cube.RasterXSize, cube.RasterYSize)

img = np.dstack((img1,img2,img3))

f = plt.figure()
plt.imshow(img)
plt.show()