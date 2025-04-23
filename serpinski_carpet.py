from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def sierpinski_carpet(x, y, z, size, depth):
    # depth >= 1. >6 - не рекомендуется, слишком много вызовов
    # идеал - size, кратный 3^depth
    # Для depth = 3: size=27, size=81, size=243
    # Для depth = 4: size=81, size=243
    if depth == 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, 35, 14)  # Установка шерсти
        return
    step = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # Центральный квадрат остается пустым
                continue
            sierpinski_carpet(x + i * step, y, z + j * step, step, depth - 1)

x, y, z = mc.player.getPos()
sierpinski_carpet(int(x), int(y), int(z), 243, 5)  # Размер = 27, глубина = 3
