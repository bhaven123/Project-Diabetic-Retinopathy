from PIL import Image
list1 = ['30_left']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    try:
        filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2

        with Image.open(filename) as image:

            #Convert the image into rgb format and save as rgb_im
            rgb_im = image.convert('RGB')

            #Determine the rgb value at position (x,y) using function rgb_im.getpixel((x,y))
            r, g, b = rgb_im.getpixel((512,512))
            print(r, g, b)

    except IOError as e:
        raise e