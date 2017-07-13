''' docstring '''

from PIL import Image

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, image_name):
        self.image_name = image_name
        self.pixel_data, self.pixel_chroma_data = None, None
        self._process_image()

    def _process_image(self):
        ''' Returns the chroma values of each pixel in the image '''
        image = Image.open(self.image_name)
        self.pixel_data = list(image.getdata())
        pixel_chroma = []
        for sets in self.pixel_data:
            chroma = max(sets[0], sets[1], sets[2]) - min(sets[0], sets[1], sets[2])
            pixel_chroma.append(chroma)
        self.pixel_chroma_data = pixel_chroma

    def get_pixel_chroma_data(self):
        ''' docstring '''
        return self.pixel_chroma_data

    def get_pixel_data(self):
        ''' docstring '''
        return self.pixel_data()

    def get_image_name(self):
        ''' docstring '''
        return self.image_name
