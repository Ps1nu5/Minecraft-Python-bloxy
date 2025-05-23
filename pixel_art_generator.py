from mcpi.minecraft import Minecraft
from PIL import Image


image = Image.open('pixel_art_small(2).png')
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
x += 2
#print(image.getpixel((1, 1)))
colors = {
    (233, 236, 236, 255): 0,
    (240, 118, 19, 255): 1,
    (189, 68, 179, 255): 2,
    (58, 175, 217, 255): 3,
    (248, 197, 39, 255): 4,
    (112, 185, 25, 255): 5,
    (237, 141, 172, 255): 6,
    (62, 68, 71, 255): 7,
    (142, 142, 134, 255): 8,
    (21, 137, 145, 255): 9,
    (121, 42, 172, 255): 10,
    (53, 57, 157, 255): 11,
    (114, 71, 40, 255): 12,
    (84, 109, 27, 255): 13,
    (160, 39, 34, 255): 14,
    (20, 21, 25, 255): 15,
}

def generate_pixelart(x, y, z, image):
    width, height = image.size
    for xi in range(width):
        for yi in range(height):
            mc.setBlock(x+xi, y, z+yi, 35, colors[image.getpixel((xi, yi))])

generate_pixelart(x, y, z, image)
