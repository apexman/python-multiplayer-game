# import _thread
# import socket
# from typing import Dict, Any
#
# from utils import convert_to_position, convert_to_bytes
#
# BUFSIZE = 2048
# POSITIONS = [(0, 0), (100, 100)]
#
# port = 9090
# # FIXME не только 2 клиента сразу должны обрабатывать, ниже дикие костыли
# available_connections_count = 2
# total_connections_count = 0
# connections: Dict[int, Any] = {}
# is_running = True
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('', port))
# server.listen(available_connections_count)
#
#
# def start_new_thread(connection):
#     global total_connections_count
#     connections_number += 1
#     connection_index = connections_number - 1
#     connections[connection_index] = connection
#     print(f"connections number: {connections_number}")
#     process_new_connection(connection_index, connections)
#     print(f"remove connection {connection_index}")
#     connections.pop(connection_index)
#     connections_number -= 1
#     print(connections)
#
#
# def process_new_connection(connection_index: int, all_connections: Dict[int, Any]) -> None:
#     """
#     Каждому новому клиенту в самом начале отдает первоначальные координаты
#     Когда клиент присылает обновление его координат, отдает новые координаты всем остальным клиентам
#     :param connection_index:
#     :param all_connections:
#     :return:
#     """
#     connection = all_connections.get(connection_index)
#     # отправляем изначальную позицию
#     connection_position = POSITIONS[connection_index]
#     connection.send(convert_to_bytes(connection_position))
#
#     try:
#         while True:
#             data = connection.recv(BUFSIZE)
#             if not data:
#                 break
#             #  сохранили изменения от текущего соединения
#             position = convert_to_position(data)
#             print(f"received from connection {connection_index} position {position}")
#             POSITIONS[connection_index] = position
#             # отправили обновление другому клиенту
#             # FIXME сейчас тип только 2 клиента могут быть, надо n клиентов
#             another_connection = all_connections.get(connection_index - 1)
#             if another_connection is not None:
#                 another_connection.send(convert_to_bytes(position))
#                 print(f"position was sent to another client")
#     except Exception as exc:
#         print("Exception")
#         print(exc)
#
#
# while True:
#     print("waiting")
#     conn, address = server.accept()
#     # обслуживаем соединение в параллельном потоке
#     _thread.start_new_thread(start_new_thread, (conn,))
