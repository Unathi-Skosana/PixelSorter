''' docstring '''
from ImageFeatureVector import ImageFeatureVector as IFV
from sys import (argv, exit)

class PixelSorter(object):
    ''' docstring '''
    def __init__(self, src_img, dest_img, sort_criteria):
        self.src_img = src_img
        self.dest_img = dest_img
        self.sort_criteria = sort_criteria
        self.__validate_args__()

    def __validate_args__(self):
        ''' docstring '''
        if not (self.sort_criteria == 'C' or self.sort_criteria == 'L'):
            raise IOError

    def pixel_sorter_middleware(self):
        ''' docstring '''
        IFV(self.src_img, self.dest_img, self.sort_criteria)

if __name__ == '__main__':
    if len(argv) == 4:
        window = PixelSorter(argv[1], argv[2], argv[3])
        window.pixel_sorter_middleware()
    else:
        exit('USAGE: python PixelSorter.py <source-img-path> <dest-img-path> <sort-criteria>')
