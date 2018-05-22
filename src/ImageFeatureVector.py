''' docstring '''

from PIL import Image

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, image_name, sort_criteria):
        self.image_name           = image_name
        self.sort_criteria        = sort_criteria
        self.pixel_data           = None
        self.criteria_data        = None
        self._process_image()

    def _process_image(self):
        ''' docstring '''
        image = Image.open(self.image_name)
        self.pixel_data = list(image.getdata())
        pixels_criteria = []
        if self.sort_criteria == 'L':
            for rgb in self.pixel_data:
                luminance = (rgb[0] * 0.3) + (rgb[1] * 0.59) + (rgb[2] * 0.11)
                pixels_criteria.append(luminance)
        elif self.sort_criteria == 'C':
            for rgb in self.pixel_data:
                chroma = max(rgb[0], rgb[1], rgb[2]) - min(rgb[0], rgb[1], rgb[2])
                pixels_criteria.append(chroma)
        self.criteria_data = pixels_criteria

    def get_criteria_data(self):
        ''' docstring '''
        return self.criteria_data

    def get_pixel_data(self):
        ''' docstring '''
        return self.pixel_data

    def get_image_name(self):
        ''' docstring '''
        return self.image_name
