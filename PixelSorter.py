''' docstring '''

import comparativeMerge
from ImageFeatureVector import ImageFeatureVector as IFV

class PixelSorter(object):
    ''' docstring '''
    def __init__(self, image_name, sort_criteria):
        self.image_name = image_name
        self.sort_criteria = sort_criteria

    def validate_args(self):
        ''' docstring '''
        if not (self.sort_criteria == 'C' or self.sort_criteria == 'L'):
            raise IOError

    def sort_pixels(self):
        ''' docstring '''
        image_feature_vector = IFV(self.image_name, self.sort_criteria)
        pixel_data = image_feature_vector.get_pixel_data()
        chroma_data = image_feature_vector.get_pixel_chroma_data()
        comparativeMerge.comparative_merge_sort(chroma_data, pixel_data)
        ''' Provide users with a visuals during the sorting '''




