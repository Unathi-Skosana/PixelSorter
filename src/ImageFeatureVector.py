''' docstring '''
import cv2
from numpy import shape, array
from math import floor
import matplotlib.pyplot as plt

class ImageFeatureVector(object):
    ''' docstring '''
    def __init__(self, img_name, dest_img_path, sort_criteria):
        self.img_name             = img_name
        self.dest_img_path        = dest_img_path
        self.sort_criteria        = sort_criteria
        self.pixel_data           = None
        self.criteria_data        = None
        self.img                  = None
        self.COLS                 = -1
        self.ROWS                 = -1
        self.r = []
        self.g = []
        self.b = []
        self.__process_img__()

    def get_color_channel(self):
        '''
        docs
        '''
        return  (self.r, self.g, self.b)

    def __process_img__(self):
        '''
        This is a helper method that is used to read in the data of the source image. This method
        gets all the pixel data of the source image to be edited.
        '''
        self.img = cv2.imread(self.img_name)
        original_image = self.img.copy()
        original_image[:, :, 0] = self.img[:, :, 2]
        original_image[:, :, 2] = self.img[:, :, 0]
        self.COLS = self.get_no_cols()/2     # divide by 2 to sort half the image
        self.ROWS = self.get_no_rows()
        self.b, self.g, self.r = cv2.split(self.img)
        for i in xrange(shape(self.b)[0]):

            temp = zip(self.r[i,...][:self.COLS], self.g[i,...][:self.COLS], self.b[i,...][:self.COLS])
            #if i % 2 != 0:
            sorted_data = self.__get_sorted__(temp, rev_status=False)
            #else:
            #    sorted_data = self.__get_sorted__(temp, rev_status=False)
            self.r[i,...][:self.COLS] = array([r for r,g,b in sorted_data])
            self.g[i,...][:self.COLS] = array([g for r,g,b in sorted_data])
            self.b[i,...][:self.COLS] = array([b for r,g,b in sorted_data])

        # do it for the next half
        for i in xrange(shape(self.b)[0]):
            temp = zip(self.r[i,...][:self.COLS], self.g[i,...][:self.COLS], self.b[i,...][:self.COLS])
            #if i % 2 == 0:
            sorted_data = self.__get_sorted__(temp, rev_status=True)
            #else:
                #sorted_data = self.__get_sorted__(temp, rev_status=False)
            self.r[i,...][self.COLS:] = array([r for r,g,b in sorted_data])
            self.g[i,...][self.COLS:] = array([g for r,g,b in sorted_data])
            self.b[i,...][self.COLS:] = array([b for r,g,b in sorted_data])

        # # NOTE: this is wrong to display an image using matplot lib. reverse the
        # (b, g, r) ->(maps to) (r, g, b)components to display on cv2.imgshow()
        # self.__show_img__('New Image', cv2.merge((self.b, self.g, self.r)))
        self.__show_img__('New Image', 'OG Image', cv2.merge((self.r, self.g, self.b)), original_image)

    def __get_sorted__(self, temp, mode='L', rev_status=False):
        new_rgb_vector = []
        if mode == 'L':
            for i in xrange(0, shape(temp)[0]):
                new_rgb_vector.append(self.get_pixel_lum(temp[i][0], temp[i][1], temp[i][2]))
        elif mode == 'C':
            for i in xrange(0, shape(temp)[0]):
                new_rgb_vector.append(self.get_pixel_chr(temp[i][0], temp[i][1], temp[i][2]))
        elif mode == 'H':
            for i in xrange(0, shape(temp)[0]):
                new_rgb_vector.append(self.get_pixel_hue(temp[i][0], temp[i][1], temp[i][2]))
        elif mode == 'B':
            for i in xrange(0, shape(temp)[0]):
                new_rgb_vector.append(self.get_pixel_bri(temp[i][0], temp[i][1], temp[i][2]))
        return [rgb for sort_criteria, rgb in sorted(zip(new_rgb_vector, temp), reverse=rev_status)]

    def __show_img__(self, new_img_status, org_img_status, new_img, org_img):
        plt.subplot(121)
        plt.title(new_img_status)
        plt.imshow(new_img)
        plt.subplot(122)
        plt.title(org_img_status)
        plt.imshow(org_img)
        plt.show()

    def get_pixel_hue(self, r, g, b):
        # TODO: fix
        # RuntimeWarning: invalid value encountered in double_scalars
        r /= 256.0; g /= 256.0; b /= 256.0
        mini, maxi = min(r, g, b), max(r, g, b)
        hue = 0.0
        if maxi == r:    hue = ((g - b) * 60.0)   / (maxi - mini)
        elif maxi == g:  hue = (2 +(b-r) * 60.0)  / (maxi - mini)
        elif maxi == b:  hue = (4 + (r-g) * 60.0) / (maxi - mini)

        if hue > 0: return floor(hue)
        else:       return floor(360 - hue)

    def get_pixel_chr(self, r, g, b):
        return max(r, g, b) - min(r, g, b)    # chroma

    def get_pixel_lum(self, r, g, b):         # luminance
        return r*0.3 + g*0.59 + b*0.11

    def get_pixel_bri(self, r, g, b):         # brightness
        # TODO: fix
        # RuntimeWarning: overflow encountered in ubyte_scalars
        return (r + g + b)*1.0 /3.0

    def get_no_rows(self):
        return self.img.shape[0]

    def get_no_cols(self):
        return self.img.shape[1]

    def is_img_clr(self):
        return self.img.shape[2] != 0

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
