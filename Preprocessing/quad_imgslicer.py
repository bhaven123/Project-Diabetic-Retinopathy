import image_slicer
list1 = ['10_left','10_right','13_left','13_right','15_left','15_right','16_left','16_right','17_left' ,'17_right']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    try:
        filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2


        tiles=image_slicer.slice(filename,4)
        print(tiles)

        #The PIL Image object can be accessed with Tile.image
        for tile in tiles:
            tile.image.show()

    except IOError as e:
        raise e