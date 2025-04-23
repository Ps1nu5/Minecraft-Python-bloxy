from mcpi.minecraft import Minecraft
from mcpi import block
import time

mc = Minecraft.create()

# Координаты, где появятся блоки-ответы
START_X, START_Y, START_Z = mc.player.getTilePos()

# Цвета блоков шерсти (wool)
colors = {
    "красный": 14,
    "оранжевый": 1,
    "жёлтый": 4,
    "зелёный": 5
}

# Список вопросов
quiz = [
    {
        "question": "Какая столица Германии?",
        "options": ["Париж", "Лондон", "Рим", "Берлин"],
        "correct_index": 3
    },
    {
        "question": "Сколько будет 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "correct_index": 1
    },
    {
        "question": "Какой цвет получается при смешении синего и жёлтого?",
        "options": ["Зелёный", "Фиолетовый", "Оранжевый", "Красный"],
        "correct_index": 0
    }
]

# Цвета по порядку для привязки к ответам
wool_order = ["красный", "оранжевый", "жёлтый", "зелёный"]

# Отображение вопроса и блоков
def ask_question(q):
    mc.postToChat("Вопрос: " + q["question"])
    time.sleep(2)
    for i, option in enumerate(q["options"]):
        color_name = wool_order[i]
        color_id = colors[color_name]
        x = START_X + i * 2
        y = START_Y
        z = START_Z + 2
        # Ставим блок шерсти нужного цвета
        mc.setBlock(x, y, z, block.WOOL.id, color_id)
        mc.postToChat(f"{i + 1}. {option} ({color_name})")
        time.sleep(1)

# Проверка позиции игрока
def check_player_answer(correct_index):
    player_pos = mc.player.getTilePos()
    chosen_index = (player_pos.x - START_X) // 2
    if chosen_index == correct_index:
        mc.postToChat("Верно!")
    else:
        mc.postToChat("Неверно!")

# Главный цикл
for q in quiz:
    ask_question(q)
    
    # Отсчёт
    for i in range(10, 0, -1):
        mc.postToChat(f"Осталось {i}...")
        time.sleep(1)
    
    check_player_answer(q["correct_index"])
    time.sleep(3)
    
    # Убираем старые блоки
    for i in range(4):
        x = START_X + i * 2
        z = START_Z + 2
        mc.setBlock(x, START_Y, z, block.AIR.id)
    time.sleep(1)

mc.postToChat("🏁 Викторина завершена!")
