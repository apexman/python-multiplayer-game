import random

#  Описываем класс Paddle, который отвечает за платформы
from position import Position


class Paddle:
    # конструктор
    def __init__(self, canvas, color):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # задаём список возможных стартовых положений платформы
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # перемешиваем их
        random.shuffle(start_1)
        # выбираем первое из перемешанных
        self.starting_point_x = start_1[0]
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 300)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаём обработчик нажатий
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # если стрелка влево — turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # пока платформа не двигается, поэтому ждём
        self.started = False
        # как только игрок нажмёт Enter — всё стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # движемся вправо
    def turn_right(self, event):
        # будем смещаться правее на 2 пикселя по оси х
        self.x = 0.2

    # движемся влево
    def turn_left(self, event):
        # будем смещаться левее на 2 пикселя по оси х
        self.x = -20

    # игра начинается
    def start_game(self, event):
        # меняем значение переменной, которая отвечает за старт движения платформы
        self.started = True

    def move(self):
        position = Position(self.canvas.coords(self.id))
        if position.left_top.x + self.x < 0 \
                or position.right_bottom.x + self.x > self.canvas_width:
            self.x = 0
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)
        self.x = 0

    # метод, который отвечает за движение платформы
    def draw(self):
        self.move()
        # получаем координаты холста
        position = Position(self.canvas.coords(self.id))
        # если мы упёрлись в левую границу
        if position.left_top.x <= 0:
            # останавливаемся
            self.x = 0
        # если упёрлись в правую границу
        elif position.right_bottom.x >= self.canvas_width:
            # останавливаемся
            self.x = 0
