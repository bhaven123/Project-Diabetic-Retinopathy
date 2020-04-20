from resizeimage import resizeimage
from PIL import Image
##############################################################
# 1.The aspect ratio of an image describes the proportional  #
# relationship between its width and height.                 #
# 2.image.size function returns a list of width and height   #
#   where size[0] is the width and size[1] is height.        #
# 3.aspect ratio is calculated as width / height             #
# 4.Using the aspect ratio new height is calculated using the#
#   new defined width of the image                           #
##############################################################

list1 = ['10_left','10_right','13_left','13_right','15_left','15_right','16_left','16_right','17_left' ,'17_right']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    try:
        filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2
        new_width = 512
        with Image.open(filename) as image:

            aspect_ratio = image.size[0] / image.size[1]
            print("Aspect Ratio:", aspect_ratio)
            print("Width:", image.size[0])
            print("Height:", image.size[1])

            new_height = int((new_width / aspect_ratio))
            print("New Width:", new_width)
            print("New Height:", new_height)

            image = resizeimage.resize_cover(image, [new_width, new_height], validate=False)
            image.save(list2, image.format)

    except IOError as e:
        raise e