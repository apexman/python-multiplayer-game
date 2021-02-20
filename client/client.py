from typing import List

from client.base_client import BaseClient
from point import Point
from utils import convert_to_point, convert_to_string


class Client(BaseClient):
    """
    Клиент для взаимодействия с сервером игры
    Когда приходит ответ от сервера, надо обновить данные в главном цикле

    Контракт взаимодействия:
        - клиент отправляет только свою позицию на сервер
        - сервер отправляет позиции всех остальных участников игры,
        таким образом, клиент по кол-ву позиций понимает сколько игроков в игре ......
    """
    # TODO сомнительно выглядит
    last_server_message: str = '50,50'

    def send(self, point: Point):
        """
        Сериализация позиции в строку и отправка на сервер
        """
        self._send(convert_to_string(point))

    def on_receive(self, data: str):
        """
        Сохранение последнего сообщения от сервера
        """
        self.last_server_message = data

    def get_last_other_players(self) -> List[Point]:
        # TODO hmmmmmm
        return [convert_to_point(self.last_server_message)]
