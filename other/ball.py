import random

from position import Position


class Ball:
    # конструктор — он вызывается в момент создания нового объекта на основе этого класса
    def __init__(self, canvas, paddle, score, color):
        # задаём параметры объекта, которые нам передают в скобках в момент создания
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # помещаем шарик в точку с координатами 245,100
        self.canvas.move(self.id, 245, 100)
        # задаём список возможных направлений для старта
        starts = [-2, -1, 1, 2]
        # перемешиваем его
        random.shuffle(starts)
        # выбираем первый из перемешанного — это будет вектор движения шарика
        self.x = starts[0]
        # в самом начале он всегда падает вниз, поэтому уменьшаем значение по оси y
        self.y = -2
        # шарик узнаёт свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # свойство, которое отвечает за то, достиг шарик дна или нет. Пока не достиг, значение будет False
        self.hit_bottom = False

    # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos
    # (левая верхняя и правая нижняя точки)
    def hit_paddle(self, position: Position):
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_position = Position(self.canvas.coords(self.paddle.random_num))
        # если координаты касания совпадают с координатами платформы
        if position.right_bottom.x >= paddle_position.left_top.x and position.left_top.x <= paddle_position.right_bottom.x:
            if paddle_position.left_top.y <= position.right_bottom.y <= paddle_position.right_bottom.y:
                # увеличиваем счёт (обработчик этого события будет описан ниже)
                self.score.hit()
                # возвращаем метку о том, что мы успешно коснулись
                return True
        # возвращаем False — касания не было
        return False

    # метод, который отвечает за движение шарика
    def draw(self):
        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        position = Position(self.canvas.coords(self.id))
        # если шарик падает сверху, position[1]
        if position.left_top.y <= 0:
            # задаём падение на следующем шаге = 2
            self.y = 2
        # если шарик правым нижним углом коснулся дна
        # position[3]
        if position.right_bottom.y >= self.canvas_height:
            # помечаем это в отдельной переменной
            self.hit_bottom = True
            # выводим сообщение и количество очков
            self.canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        # если было касание платформы
        if self.hit_paddle(position):
            # отправляем шарик наверх
            self.y = -2
        if position.right_bottom.y >= self.canvas_height:
            self.y = -2
        # если коснулись левой стенки
        # position[0]
        if position.left_top.x <= 0:
            # движемся вправо
            self.x = 2
        # если коснулись правой стенки
        # position[2]
        if position.right_bottom.x >= self.canvas_width:
            # движемся влево
            self.x = -2
