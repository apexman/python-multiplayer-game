#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    # конструктор
    def __init__(self, canvas, color):
        # в самом начале счёт равен нулю
        self.score = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт, делаем его нужно цвета и запоминаем внутреннее имя этой надписи
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    # обрабатываем касание платформы
    def hit(self):
        # увеличиваем счёт на единицу
        self.score += 1
        # пишем новое значение счёта
        self.canvas.itemconfig(self.id, text=self.score)
