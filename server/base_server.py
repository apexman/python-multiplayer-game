import _thread
import socket
from typing import Dict, Any

from point import Point
from utils import convert_to_point, convert_to_string

POINTS = [Point(100, 100), Point(100, 100)]


class BaseServer:
    BUFSIZE = 2048

    server: socket
    port = 9090
    available_connections_count = 2
    total_connections_count = 0
    connections: Dict[int, Any] = {}

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.server = s
            # try to reuse socket
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind(('', self.port))
            self.server.listen(self.available_connections_count)
            while True:
                print("waiting")
                conn, address = self.server.accept()
                # обслуживаем соединение в параллельном потоке
                _thread.start_new_thread(self.process_new_connection, (conn,))

    def process_new_connection(self, connection):
        with connection:
            self.total_connections_count += 1
            connection_index = self.total_connections_count - 1
            self.connections[connection_index] = connection
            print("----------")
            print(f"new connection with index {connection_index}")
            print(f"total connections count: {self.total_connections_count}")
            self.receive(connection_index)
            print(f"remove connection with index {connection_index}")
            self.connections.pop(connection_index)
            self.total_connections_count -= 1
            print(f"connection indices {self.connections.keys()}")

    def receive(self, connection_index: int) -> None:
        connection = self.connections.get(connection_index)
        connection.send(bytes(str(connection_index), "UTF-8"))

        try:
            while True:
                data = connection.recv(self.BUFSIZE)
                if not data:
                    break
                data_decode = data.decode("UTF-8")
                print(f"received from connection '{connection_index}' data '{data_decode}'")
                self.update_context(connection_index, data_decode)
                # отправили обновление другому клиенту
                # FIXME сейчас тип только 2 клиента могут быть, надо n клиентов
                another_connection_index = 0 if connection_index == 1 else 1
                another_connection = self.connections.get(another_connection_index)
                if another_connection is not None:
                    data = bytes(convert_to_string(POINTS[connection_index]), "UTF-8")
                    another_connection.send(data)
                    print(f"data was sent to another client")
        except Exception as exc:
            print("Exception")
            print(exc)

    def update_context(self, connection_index: int, data_decode: str):
        point = convert_to_point(data_decode)
        POINTS[connection_index] = point
