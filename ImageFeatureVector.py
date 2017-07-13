''' docstring '''

from PIL import Image

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, imagename):
        self.imagename = imagename

    def getpixelchroma(self):
        ''' Returns the chroma values of each pixel in the image '''
        image = Image.open(self.imagename)
        pixeldata = list(image.getdata())
        pixelchroma = []
        for sets in pixeldata:
            chroma = max(sets[0], sets[1], sets[2]) - min(sets[0], sets[1], sets[2])
            pixelchroma.append(chroma)
        return pixelchroma

    def get_image_name(self):
        ''' docstring '''
        return self.imagename

''' Add more sorting criteria'''