from PIL import Image
 
def flip_image(image_path, saved_location):

    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
    #rotated_image.show()
 
#if __name__ == '__main__':
#    image = '1img_00011.jpg'
#    flip_image(image, '1img_00011_flipped.jpg')
    

import os
for fname in os.listdir('.'):
    image = fname
    base = os.path.splitext(fname)[0]
    flip_image(image, base+'01.jpg')
