from PIL import Image
from resizeimage import resizeimage
list1 = ['10_left','10_right','13_left','13_right','15_left','15_right','16_left','16_right','17_left' ,'17_right']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    try:
        filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2

        with Image.open(filename) as image:
            image.show(title="Original")

            #Calculate aspect ratio where image.size[0] is width & image.size[1] is height
            aspect_ratio = image.size[0] / image.size[1]

            #Compute new height keeping width constant as 512
            new_width = 512
            new_height = int((new_width / aspect_ratio))

            #resize and display
            #image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
            image = image.resize((new_width,new_height), Image.ANTIALIAS)
            image.show(title="Resized")

    except IOError as e:
        raise e