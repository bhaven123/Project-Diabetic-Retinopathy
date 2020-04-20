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

            #image.split() returns a tuple comprising of 3 images, one for each r, g & b
            print(image.split())

            image.split()[0].show()
            image.split()[1].show()
            image.split()[2].show()

    except IOError as e:
        raise e