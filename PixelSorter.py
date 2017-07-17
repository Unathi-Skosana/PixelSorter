''' docstring '''

from utils.ComparativeMerge import comparative_merge_sort
from utils.ImageFeatureVector import ImageFeatureVector as IFV

class PixelSorter(object):
    ''' docstring '''
    def __init__(self, image_name, sort_criteria):
        self.image_name = image_name
        self.sort_criteria = sort_criteria
        self._validate_args()

    def _validate_args(self):
        ''' docstring '''
        if not (self.sort_criteria == 'C' or self.sort_criteria == 'L'):
            raise IOError

    def sort_pixels(self):
        ''' docstring '''
        ifv           = IFV(self.image_name, self.sort_criteria)
        pixel_data    = ifv.get_pixel_data()
        criteria_data = ifv.get_criteria_data()
        comparative_merge_sort(criteria_data, pixel_data)

if __name__ == '__main__':
    window = PixelSorter('./tests/test_cases/colorful.jpg', 'C')
    window.sort_pixels()
