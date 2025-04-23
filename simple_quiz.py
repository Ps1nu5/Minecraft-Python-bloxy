from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

pos = mc.player.getTilePos()

start_x = pos.x
start_y = pos.y+20
start_z = pos.z

fail_count = 0

mc.setBlocks(start_x-3, start_y, start_z-3, start_x+3, start_y, start_z+3, 44)

mc.setBlock(start_x+5, start_y, start_z, 1)
mc.setBlock(start_x+5, start_y+1, start_z, 51)

mc.setBlocks(start_x+5, start_y+4, start_z, start_x+5, start_y+4-fail_count, start_z, 46)


mc.player.setTilePos(start_x, start_y+1, start_z)



mc.postToChat('Добро пожаловать')
time.sleep(1)
mc.postToChat('Правила....')
time.sleep(2)

mc.postToChat('Вопрос 1.')
mc.postToChat('Какой-то вопрос(выбрать изумруд)')

mc.setBlock(start_x+2, start_y, start_z, 14)
mc.setBlock(start_x+2, start_y, start_z-2, 129)
mc.setBlock(start_x+2, start_y, start_z+2, 15)

time.sleep(7)

x, y, z = mc.player.getTilePos()
if mc.getBlock(x, y-1, z) == 129:
    mc.postToChat('Правильно!')
else:
    mc.postToChat('Неправильно! Ты на шаг ближе к взрыву!')
    fail_count += 1

mc.setBlocks(start_x+5, start_y+4, start_z, start_x+5, start_y+4-fail_count, start_z, 46)
mc.setBlock(start_x+5, start_y+1, start_z, 51)


mc.setBlocks(start_x-3, start_y, start_z-3, start_x+3, start_y, start_z+3, 44)
mc.player.setTilePos(start_x, start_y+1, start_z)

mc.postToChat('Вопрос 2.')
mc.postToChat('Какой-то вопрос(выбрать шерсть)')

mc.setBlock(start_x+2, start_y, start_z, 35)
mc.setBlock(start_x+2, start_y, start_z-2, 5)
mc.setBlock(start_x+2, start_y, start_z+2, 18)

time.sleep(7)

x, y, z = mc.player.getTilePos()
if mc.getBlock(x, y-1, z) == 35:
    mc.postToChat('Правильно!')
else:
    mc.postToChat('Неправильно! Ты на шаг ближе к взрыву!')
    fail_count += 1

mc.setBlocks(start_x+5, start_y+4, start_z, start_x+5, start_y+4-fail_count, start_z, 46)
mc.setBlock(start_x+5, start_y+1, start_z, 51)
