from PIL import Image;
import comparativeMerge;

class PixelSorter(object):
    def __init__(self, imageName, sortCreateria):
        self.imageName = imageName
        self.sortCreateria = sortCreateria;

    def validateArgs(self):
        if not (self.sortCreateria == 'C' or self.sortCreateria == 'L'):
            return IOError;
        else:
            pass

    def sortPixels(self):


