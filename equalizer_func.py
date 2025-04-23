from mcpi import minecraft
import random
import time

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getTilePos()
x += 2

def build_column(x, y, z, height, block_id):
    mc.setBlocks(x, y, z, x, y+10, z, 0)
    mc.setBlocks(x, y, z, x, y+height, z, 35, block_id)


def create_equalizer(width):
    for i in range(width):
        wool_id = random.randint(0, 15)
        height = random.randint(1, 10)
        build_column(x+i, y, z, height, wool_id)

while True:
    create_equalizer(5)
    time.sleep(0.5)
