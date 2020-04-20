from PIL import Image


class preprocess:
    def __init__(self,f):
        self.filename=f

        try:
            self.image=Image.open(filename)

        except IOError as e:
            raise e

    def resize(self):
        self.image.show(title="Original")

        #Calculate aspect ratio where image.size[0] is width & image.size[1] is height
        aspect_ratio = self.image.size[0] / self.image.size[1]

        #Compute new height keeping width constant as 512
        new_width = 512
        new_height = int((new_width / aspect_ratio))

        #resize and display
        #image = resizeimage.resize_cover(image, [new_width, new_height], validate = False)
        self.image = self.image.resize((new_width,new_height), Image.ANTIALIAS)
        self.image.show(title="Resized")

    def quadrants(self):
        width=self.image.size[0]
        height=self.image.size[1]
        half_width=width//2
        half_height=height//2

        #image.crop(x1,y1,x2,y2) crops the image taking as input (x1,y1):top left co-ordinates & (x2,y2):bottom right co-ordinates

        #Quadrant 1
        self.image.crop((half_width,0,width,half_height)).show()

        #Quadrant 2
        self.image.crop((0,0,half_width,half_height)).show()

        #Quadrant 3
        self.image.crop((0,half_height,half_width,height)).show()

        #Quadrant 4
        self.image.crop((half_width,half_height,width,height)).show()

    def rgb(self):
        #image.split() returns a tuple comprising of 3 images, one for each r, g & b
        print(self.image.split())

        self.image.split()[0].show()
        self.image.split()[1].show()
        self.image.split()[2].show()
list1 = ['10_left','10_right','13_left','13_right','15_left','15_right','16_left','16_right','17_left' ,'17_right']
i = 0
while i < len(list1):
    list2 = list1[i]+'.jpeg'
    i += 1
    print(list2)
    filename = 'E:\\Project\\Diabetic Retinopathy\\check\\' + list2
    obj = preprocess(filename)
    obj.resize()
    obj.rgb()
    obj.quadrants()