# from PIL import Image
# im = Image.open('g_i33a1.tiff')
# im.show()

#################################

from PIL import Image, ImageFont, ImageDraw
from osgeo import gdal,ogr

image = 'g_i33a1.tiff'
src_ds = gdal.Open(image)
gt = src_ds.GetGeoTransform() # used to convert geographical coordinates to pixel coordinates

# font = ImageFont.truetype("sans-serif", 16)

img = Image.open(image)

def add_marker (gt, watermark, font, img, mx, my, text):
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel


    wmark = Image.open(watermark)
    draw = ImageDraw.Draw(wmark)
    draw.text((12, 10), text, (0, 0, 0), font=font)

    img.paste(wmark, (px, py), wmark)

# add_marker(gt, 'marker1.png', font, img, 0.012, 0.0132, "1")

img.save("result.png", "PNG")