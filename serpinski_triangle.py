from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def draw_line_simple(x1, y1, z1, x2, y2, z2, block_id, block_data=0):
    """
    Рисует линию между двумя точками (x1, y1, z1) и (x2, y2, z2).
    :param x1, y1, z1: Координаты начальной точки.
    :param x2, y2, z2: Координаты конечной точки.
    :param block_id: ID блока.
    :param block_data: Дополнительные данные блока (например, цвет шерсти).
    """
    # Вычисляем длину линии
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    distance = max(abs(dx), abs(dy), abs(dz))  # Максимальное расстояние для шага

    if distance == 0:
        # Если точки совпадают, устанавливаем один блок
        mc.setBlock(x1, y1, z1, block_id, block_data)
        return

    # Шаги для каждой оси
    step_x = dx / distance
    step_y = dy / distance
    step_z = dz / distance

    # Устанавливаем блоки вдоль линии
    for i in range(int(distance) + 1):
        x = round(x1 + step_x * i)
        y = round(y1 + step_y * i)
        z = round(z1 + step_z * i)
        mc.setBlock(x, y, z, block_id, block_data)



def draw_triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3, block_id=35, block_data=14):
    """Рисует треугольник из блоков."""
    # Устанавливаем блоки вдоль сторон треугольника
    draw_line_simple(x1, y1, z1, x2, y2, z2, block_id, block_data)
    draw_line_simple(x2, y2, z2, x3, y3, z3, block_id, block_data)
    draw_line_simple(x3, y3, z3, x1, y1, z1, block_id, block_data)

def sierpinski_triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3, depth, block_id=35, block_data=14):
    """Рекурсивно строит треугольник Серпинского."""
    if depth == 0:
        draw_triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3, block_id, block_data)
        return
    
    # Находим координаты средних точек для разбиения треугольника
    mx1 = (x1 + x2) // 2
    mz1 = (z1 + z2) // 2
    mx2 = (x2 + x3) // 2
    mz2 = (z2 + z3) // 2
    mx3 = (x3 + x1) // 2
    mz3 = (z3 + z1) // 2

    # Рекурсивно строим 3 внешних треугольника
    sierpinski_triangle(x1, y1, z1, mx1, y1, mz1, mx3, y1, mz3, depth - 1, block_id, block_data)
    sierpinski_triangle(mx1, y1, mz1, x2, y1, z2, mx2, y1, mz2, depth - 1, block_id, block_data)
    sierpinski_triangle(mx3, y1, mz3, mx2, y1, mz2, x3, y1, z3, depth - 1, block_id, block_data)

# Начальные координаты треугольника
x, y, z = mc.player.getPos()
size = 64  # Размер треугольника
sierpinski_triangle(x, y, z, x + size, y, z, x + size // 2, y, z + size, 5, block_id=35, block_data=5)
