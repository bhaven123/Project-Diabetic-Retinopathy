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

            #p=width, q=height, m=half of width, n=half of height
            p=image.size[0]
            q=image.size[1]
            m=p//2
            n=q//2
            print(p,q,m,n)

            #image.crop(x1,y1,x2,y2) crops the image taking as input (x1,y1):top left co-ordinates & (x2,y2):bottom right co-ordinates

            #Quadrant 1
            image.crop((m,0,p,n)).show()

            #Quadrant 2
            image.crop((0,0,m,n)).show()

            #Quadrant 3
            image.crop((0,n,m,q)).show()

            #Quadrant 4
            image.crop((m,n,p,q)).show()

    except IOError as e:
        raise e