# import socket
# from typing import Tuple, Optional
#
# from utils import convert_to_bytes, convert_to_position
#
# BUFSIZE = 2048
#
#
# class Client:
#     ip = ""
#     port = 9090
#
#     def __init__(self):
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.socket.connect((self.ip, self.port))
#
#     def send(self, data: Optional[Tuple]):
#         outgoing = convert_to_bytes(data) if data else None
#         self.socket.send(outgoing)
#         print(f"sent {data}")
#
#     def receive(self) -> Optional[Tuple]:
#         print("kekekek try to receive")
#         data = self.socket.recv(BUFSIZE)
#         data = convert_to_position(data) if data else None
#         print(f"received {data}")
#         return data
#
#     def stop(self):
#         self.socket.close()
#
#
# client = Client()
# while True:
#     text = input("vvedi text")
#     client.send(text)
