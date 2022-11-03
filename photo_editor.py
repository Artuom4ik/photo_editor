from PIL import Image

image = Image.open("example.jpg")
rgb_image = image.convert("RGB")

red, green, blue = image.split()

coordinates = (50, 0, red.width, red.height)
red_image_left = red.crop(coordinates)
cords = (25, 0, red.width - 25, red.height)
red_image_middle = red.crop(cords)

red_image_3 = Image.blend(red_image_middle, red_image_left, 0.5)

coordinates = (50, 0, red.width, red.height)
blue_image_left = blue.crop(coordinates)
cords = (25, 0, red.width - 25, red.height)
blue_image_middle = blue.crop(cords)

blue_image3 = Image.blend(blue_image_middle, blue_image_left, 0.5)

coords = (25, 0, green.width - 25, green.height)
green_image_middle = green.crop(coords)

new_example = Image.merge("RGB",
                          (red_image_3, green_image_middle, blue_image3))
new_example.save('new_example.jpg')

avatar = Image.open("new_example.jpg")
avatar.thumbnail((200, 200))  
avatar.save('avatar.jpg')
