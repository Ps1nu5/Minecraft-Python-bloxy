from mcpi.minecraft import Minecraft
from opensimplex import OpenSimplex  
import random

# Подключение к Minecraft
mc = Minecraft.create()

# Параметры для генерации ландшафта
print("Генерация трёхмерного ландшафта...")
# width = int(input("Введите ширину ландшафта: "))
# depth = int(input("Введите глубину ландшафта: "))
# base_height = int(input("Введите базовую высоту: "))
# amplitude = int(input("Введите амплитуду колебаний: "))
# scale = float(input("Введите масштаб шума (рекомендуется 10-50): "))
width = 50
depth = 50
base_height = 1
amplitude = 15
scale = 40
sea_level = 2

# Инициализация генератора шума Симплекса
seed = random.randint(0, 1000)
simplex = OpenSimplex(seed)

# Генерация двумерного массива высот
heights = []
for x in range(width):
    row = []
    for z in range(depth):
        # Вычисляем значение шума для текущей точки
        noise_value = simplex.noise2(x / scale, z / scale)
        # Преобразуем значение шума в высоту
        height = int(base_height + noise_value * amplitude)
        row.append(max(1, height))  # Ограничиваем минимальную высоту
    heights.append(row)

# for line in heights:
#     print(line)

player_postition = mc.player.getTilePos()
start_x, start_y, start_z = player_postition.x, player_postition.y, player_postition.z

block_stone = 1
block_dirt = 2
block_sand = 12
block_water = 9
block_air = 0

max_height = 0

for line in heights:
    for i in line:
        if i > max_height:
            max_height = i

third = max_height // 3

for x in range(len(heights)):
    for z in range(len(heights[x])):
        height = heights[x][z]

        for y in range(start_y, start_y+height):
            if y < start_y + third:
                block_type = block_sand
            elif y < start_y + third*2:
                block_type = block_dirt
            else:
                if random.randint(1, 15) == 1:
                    block_type = 15
                elif random.randint(1, 10) == 1:
                    block_type = 16
                else:
                    block_type = block_stone
            
            mc.setBlock(start_x+x, y, start_z+z, block_type)

        for y in range(start_y, start_y+sea_level):
            if y >= start_y + height:
                mc.setBlock(start_x+x, y, start_z+z, block_water)


