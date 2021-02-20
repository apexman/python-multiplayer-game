from tkinter import Canvas
from typing import Any

from point import Point


class Player:
    """
    Создается "игрок" - создается фигура текущего игрока в канвасе
    Все фигуры контролируются главным циклом, т.е на момент отрисовки фигуры ее может уже не быть на канвасе
    """

    canvas: Canvas
    canvas_width: Any
    canvas_height: Any
    id: str
    point: Point
    color: str
    is_point_sent: bool = False

    def __init__(self, canvas: Canvas, color: str, starting_point: Point):
        """
        Создается фигура с заданными координатами
        """
        self.canvas: Canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.color = color
        self.point = starting_point

        self.create_figure()

    def create_figure(self):
        self.id = self.canvas.create_rectangle(0, 0, 10, 10, fill=self.color)
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.point.x, self.point.y)

    def get_point(self) -> Point:
        return self.point


class MainPlayer(Player):
    velx: int = 0
    vely: int = 0

    W_KEY_NAMES = ["w", "ц", "1"]
    A_KEY_NAMES = ["a", "ф", "2"]
    S_KEY_NAMES = ["s", "ы", "3"]
    D_KEY_NAMES = ["d", "в", "4"]

    def __init__(self, canvas: Canvas, color: str, starting_point: Point):
        super(MainPlayer, self).__init__(canvas, color, starting_point)
        self.bind_keys()

    def bind_keys(self):
        self.canvas.bind_all("<KeyPress>", self.key_press)
        self.canvas.bind_all("<KeyRelease>", self.key_release)

    def redraw(self):
        self.move()
        self.create_figure()

    def move(self):
        self.point.x += self.velx
        self.point.y += self.vely
        if self.velx != 0 or self.vely != 0:
            self.is_point_sent = False

    # region

    def key_press(self, event):
        print(event)
        pressed_key_name = event.char
        if pressed_key_name in self.A_KEY_NAMES:
            self.velx = -5
        if pressed_key_name in self.D_KEY_NAMES:
            self.velx = 5
        if pressed_key_name in self.W_KEY_NAMES:
            self.vely = -5
        if pressed_key_name in self.S_KEY_NAMES:
            self.vely = 5

    def key_release(self, event):
        print(event)
        released_key_name = event.char
        if released_key_name in self.A_KEY_NAMES or released_key_name in self.D_KEY_NAMES:
            self.velx = 0
        if released_key_name in self.W_KEY_NAMES or released_key_name in self.S_KEY_NAMES:
            self.vely = 0
