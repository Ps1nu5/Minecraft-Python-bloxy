from mcpi.minecraft import Minecraft
import random
import time

# Подключение к Minecraft
mc = Minecraft.create()

# Размеры куба
cube_size = 10

# Количество блоков алмазной руды
diamond_blocks_count = 5

# ID блока алмазной руды
DIAMOND_ORE = 56

# Функция для создания куба
def create_cube(x, y, z, size, block_type):
    mc.setBlocks(x, y, z, x + size - 1, y + size - 1, z + size - 1, block_type)

# Функция для генерации случайных координат внутри куба
def generate_random_coordinates(cube_x, cube_y, cube_z, size, count):
    coordinates = []
    while len(coordinates) < count:
        x = random.randint(cube_x, cube_x + size - 1)
        y = random.randint(cube_y, cube_y + size - 1)
        z = random.randint(cube_z, cube_z + size - 1)
        if (x, y, z) not in coordinates:  # Убедимся, что координаты уникальны
            coordinates.append((x, y, z))
    return coordinates

# Получаем текущую позицию игрока
player_position = mc.player.getTilePos()
cube_x, cube_y, cube_z = player_position.x, player_position.y, player_position.z

# Создаём куб из камня
create_cube(cube_x, cube_y, cube_z, cube_size, 1)

# Генерируем случайные координаты для алмазной руды
diamond_coordinates = generate_random_coordinates(cube_x, cube_y, cube_z, cube_size, diamond_blocks_count)

# Размещаем блоки алмазной руды
for coord in diamond_coordinates:
    mc.setBlock(coord[0], coord[1], coord[2], DIAMOND_ORE)

# Выводим сообщение о начале игры
mc.postToChat("Найдите и уничтожьте все блоки алмазной руды!")

# Записываем время начала игры
start_time = time.time()

# Основной игровой цикл
while diamond_coordinates:
    for coord in diamond_coordinates[:]:  # Используем копию списка для безопасного удаления
        block_id = mc.getBlock(coord[0], coord[1], coord[2])
        if block_id != DIAMOND_ORE:  # Если блок уничтожен
            diamond_coordinates.remove(coord)
            mc.postToChat(f"Блок алмазной руды найден! Осталось: {len(diamond_coordinates)}")
    
    # Добавляем небольшую задержку, чтобы не перегружать процессор
    time.sleep(0.5)

# Вычисляем время, затраченное на игру
end_time = time.time()
elapsed_time = round(end_time - start_time, 2)

# Выводим сообщение о победе
mc.postToChat(f"Победа! Все блоки алмазной руды уничтожены за {elapsed_time} секунд.")
