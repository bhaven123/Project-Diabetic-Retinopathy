from PIL import Image
list1 = ['10_left','10_right','13_left','13_right','15_left','15_right','16_left','16_right','17_left' ,'17_right']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    try:
        filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2

        with Image.open(filename) as image:

            #aspect_ratio = image.size[0] / image.size[1]
            #print("Aspect Ratio:", aspect_ratio)
            print("Width:", image.size[0])
            print("Height:", image.size[1])
            print(image.palette)
            m=image.size[0]//2
            n=image.size[1]//2
            print(image.getcolors(maxcolors=256))
            print(image.split()[2].show())
            #print(image.getpixel(12))

            rgb_im = image.convert('RGB')
            r, g, b = rgb_im.getpixel((512,512))
            print(r, g, b)
        #crop=image.crop((0,0,m,n))
        #crop.load()
        #crop.save("C:/Users/sniha/Desktop/DR/1",image.format)

        #image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
        #image.save(list2, image.format)

    except IOError as e:
        raise e
