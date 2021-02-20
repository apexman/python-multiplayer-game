from tkinter import Tk, Canvas
from typing import List

from client.client import Client
from client.player import Player, MainPlayer
from point import Point


class Game:
    """
    Здесь находится главный цикл игры
    Создается канвас для отрисовки всех переданных объектов
    Создается фигурка игрока, за которого он играет
    Отрисовываются все фигурки игроков, которые передал сервер
    """

    is_running = True
    tk: Tk
    canvas: Canvas
    client: Client
    main_player: MainPlayer
    other_players: List[Player] = []

    def __init__(self):
        """
        создается канвас
        создается и отрисовывается игрок
        создается соединение с сервером
        """
        self.create_main_window()
        self.create_main_player()
        self.create_connection()

    def create_main_window(self):
        self.tk = Tk()
        self.tk.title("eBall game")
        self.tk.resizable(0, 0)
        # помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить
        self.tk.wm_attributes('-topmost', 1)
        self.canvas = Canvas(self.tk, width=600, height=600, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

    def create_main_player(self):
        self.main_player = MainPlayer(self.canvas, 'red', Point(100, 100))

    def create_connection(self):
        self.client = Client()

    def start(self):
        """
        Запускается главный цикл отрисовки
        """
        self.draw()
        self.tk.mainloop()

    def draw(self):
        """
        Главный цикл отрисовки объектов на канвасе
        Описание такта:
            - считываются последние данные с сервера
            - очищается канвас
            - отрисовывается позиция текущего игрока
            - отрисовываются все остальные игроки, согласно контракту
            - позиция игрока отправляется на сервер
        """
        if self.is_running:
            other_players_positions = self.client.get_last_other_players()
            self.clear_main_window()
            self.redraw_main_player()
            self.redraw_other_players(other_players_positions)
            self.send_main_player_position()
            self.tk.after(10, self.draw)

    def clear_main_window(self):
        self.canvas.delete("all")

    def redraw_main_player(self):
        self.main_player.redraw()

    def redraw_other_players(self, other_players_points: List[Point]):
        for player_point in other_players_points:
            Player(self.canvas, 'red', player_point)

    def send_main_player_position(self):
        if not self.main_player.is_point_sent:
            self.client.send(self.main_player.get_point())
            self.main_player.is_point_sent = True
