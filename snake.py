from mcpi.minecraft import Minecraft
import random
import time

# Подключение к Minecraft
mc = Minecraft.create()

# ID блоков
SNAKE_BLOCK = 35  # Шерсть (белый цвет)
FOOD_BLOCK = 14   # Золотой блок
CONTROL_BLOCKS = {
    "up": 5,       # Дерево (вверх)
    "down": 2,     # Камень (вниз)
    "left": 41,    # Золотой блок (влево)
    "right": 57    # Алмазный блок (вправо)
}

# Размеры игрового поля
FIELD_SIZE = 10

# Начальная позиция змеи
snake = [(0, 0)]  # Список координат змеи (голова - первый элемент)

# Начальное направление движения (x, y)
direction = (1, 0)

# Генерация случайной еды
def generate_food():
    while True:
        food_x = random.randint(-FIELD_SIZE // 2, FIELD_SIZE // 2)
        food_y = random.randint(0, FIELD_SIZE // 2)  # Еда только выше нулевого уровня
        if (food_x, food_y) not in snake:
            return food_x, food_y

# Построение платформы управления и игрового поля
def setup_game(player_position):
    px, py, pz = player_position.x, player_position.y, player_position.z

    # Платформа управления (блоки под игроком)
    mc.setBlocks(px - 1, py - 1, pz - 1, px + 1, py - 1, pz + 1, 44)  # Каменные плиты
    mc.setBlock(px, py - 1, pz + 1, CONTROL_BLOCKS["up"])  # Дерево (вверх)
    mc.setBlock(px, py - 1, pz - 1, CONTROL_BLOCKS["down"])  # Камень (вниз)
    mc.setBlock(px - 1, py - 1, pz, CONTROL_BLOCKS["left"])  # Золотой блок (влево)
    mc.setBlock(px + 1, py - 1, pz, CONTROL_BLOCKS["right"])  # Алмазный блок (вправо)

    # Игровое поле (вертикальное)
    mc.setBlocks(px - FIELD_SIZE // 2, py + 2, pz + 5,
                 px + FIELD_SIZE // 2, py + FIELD_SIZE + 2, pz + 5, 0)  # Очистка поля
    mc.setBlocks(px - FIELD_SIZE // 2, py + 2, pz + 5,
                 px + FIELD_SIZE // 2, py + FIELD_SIZE + 2, pz + 5, 35, 7)  # Серая шерсть (фон)

# Главная логика игры
def main():
    # Получаем текущую позицию игрока
    player_position = mc.player.getTilePos()
    px, py, pz = player_position.x, player_position.y, player_position.z

    # Телепортируем игрока на платформу управления
    mc.player.setTilePos(px+1, py, pz)

    # Настройка игры
    setup_game(player_position)
    food = generate_food()

    # Размещение начальной змеи и еды
    for x, y in snake:
        mc.setBlock(px + x, py + y + 2, pz + 5, SNAKE_BLOCK)
    mc.setBlock(px + food[0], py + food[1] + 2, pz + 5, FOOD_BLOCK)

    global direction

    # Главный игровой цикл
    while True:
        # Проверка управления через блоки
        player_tile = mc.player.getTilePos()
        pxp, pyp, pzp = player_tile.x, player_tile.y, player_tile.z

        # Определяем блок под игроком
        block_under_player = mc.getBlock(pxp, pyp - 1, pzp)

        if block_under_player == CONTROL_BLOCKS["up"]:  # Дерево (вверх)
            direction = (0, 1)
        elif block_under_player == CONTROL_BLOCKS["down"]:  # Камень (вниз)
            direction = (0, -1)
        elif block_under_player == CONTROL_BLOCKS["left"]:  # Золотой блок (влево)
            direction = (-1, 0)
        elif block_under_player == CONTROL_BLOCKS["right"]:  # Алмазный блок (вправо)
            direction = (1, 0)

        # Движение змеи
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Проверка на выход за границы поля
        if abs(new_head[0]) > FIELD_SIZE // 2 or new_head[1] < 0 or new_head[1] > FIELD_SIZE:
            mc.postToChat("Игра окончена! Вы вышли за границы.")
            break

        # Проверка на столкновение с собой
        if new_head in snake:
            mc.postToChat("Игра окончена! Вы врезались в себя.")
            break

        # Добавление новой головы
        snake.insert(0, new_head)


        # Проверка на съедение еды
        if new_head == food:
            food = generate_food()
            mc.setBlock(px + food[0], py + food[1] + 2, pz + 5, FOOD_BLOCK)
            mc.postToChat(f"Еда съедена! Текущая длина змеи: {len(snake)}")
        else:
            # Удаление хвоста
            tail = snake.pop()
            mc.setBlock(px + tail[0], py + tail[1] + 2, pz + 5, 35, 7)  # Фоновое поле

        # Обновление блоков змеи
        for x, y in snake:
            mc.setBlock(px + x, py + y + 2, pz + 5, SNAKE_BLOCK)

        # Добавляем задержку для управления скоростью игры
        time.sleep(1)

# Запуск игры
if __name__ == "__main__":
    main()
