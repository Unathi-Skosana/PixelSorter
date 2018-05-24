''' docstring '''
import cv2
from numpy import shape
"""
# TODO: remove or change the main library from PIL -> cv2
"""

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, img_name, dest_img_path, sort_criteria):
        self.img_name             = img_name
        self.dest_img_path        = dest_img_path
        self.sort_criteria        = sort_criteria
        self.pixel_data           = None
        self.criteria_data        = None
        self.img                  = None
        self.__process_img__()

    def __process_img__(self):
        '''
        This is a helper method that is used to read in the data of the source image. This method
        gets all the pixel data of the source image to be edited.
        '''
        self.img = cv2.imread(self.img_name)
        lum = lambda r, g, b: r*0.3 + g*0.59 + b*0.11        # luminance
        chr = lambda r, g, b: max(r, g, b) - min(r, g, b)    # chroma

        self.__show_src_img__('Source Image', self.img)


        #self.pixel_data = self.img.getdata()
        #pixels_criteria = []
        #if self.sort_criteria == 'L':
        #    for (r, g, b) in self.pixel_data:
        #        pixels_criteria.append(lum(r, g, b))
        #elif self.sort_criteria == 'C':
        #    for r, g, b in self.pixel_data:
        #        pixels_criteria.append(chr(r, g, b))
        #self.criteria_data = pixels_criteria
        pass

    def __show_src_img__(self, img_name, img):
        cv2.imshow(img_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_no_rows(self): return self.img.shape[0]

    def get_no_cols(self): return self.img.shape[1]

    def is_img_clr(self):  return self.img.shape[2] == 0

    def create_sorted_img(self, criteria_data, pixel_data):
        '''
        this method is responseble for writing the final edited or sorted image to the
        destination path
        '''
        pass

    #def view_edt_img(self):
    #    pass

    def get_criteria_data(self):
        '''
        my name oi u bhejlo mpi;o ewhf jsdhfjkh sdajfhjsdajkfkj jsdhfjk safh sdajf hkhf # HACK: k
        dsjkfhkjdsh sdjfh sdkjfh kjsdahfjksadfh ksdjafh sdkajfh sdajkfhkjsdafh
        '''
        return self.criteria_data

    def get_pixel_data(self):
        '''
        get the data for individual pixels, the return type of this method is a length
        3 turple that has individual pixel RGB data. NOTE: these are actually the original
        pixel data of the image that was read from the source image to be edited
        '''
        return self.pixel_data

    def get_img_destination_path(self):
        '''
        returns the destination or path of the resulting image, that has been sorted.
        '''
        return self.dest_img_path

    def get_image_name(self):
        '''
        returns the original image name that was being sorted or that was being edited.
        '''
        return self.img_name
