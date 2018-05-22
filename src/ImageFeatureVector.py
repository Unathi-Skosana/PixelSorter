''' docstring '''

from PIL import Image

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, img_name, sort_criteria):
        self.img_name             = img_name
        self.sort_criteria        = sort_criteria
        self.pixel_data           = None
        self.criteria_data        = None
        self.__process_img__()

    def __process_img__(self):
        ''' docstring '''
        img = Image.open(self.img_name)
        lum = lambda r, g, b: r*0.3 + g*0.59 + b*0.11        # luminance
        chr = lambda r, g, b: max(r, g, b) - min(r, g, b)    # chroma
        self.pixel_data = list(img.getdata())
        pixels_criteria = []
        if self.sort_criteria == 'L':
            for rgb in self.pixel_data:
                pixels_criteria.append(lum(rgb[0], rgb[1], rgb[2]))
        elif self.sort_criteria == 'C':
            for rgb in self.pixel_data:
                pixels_criteria.append(chr(rgb[0], rgb[1], rgb[2]))
        self.criteria_data = pixels_criteria

    def get_criteria_data(self):
        ''' docstring '''
        return self.criteria_data

    def get_pixel_data(self):
        ''' docstring '''
        return self.pixel_data

    def get_image_name(self):
        ''' docstring '''
        return self.img_name
