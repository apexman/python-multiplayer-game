import _thread
import socket
from typing import Optional


class BaseClient:
    BUFSIZE = 2048

    ip = "127.0.0.1"
    port = 9090
    is_running = True
    was_connected = False
    connection: socket = None
    connection_index: str = None

    def __init__(self):
        # TODO used low-level _thread w/o locks
        _thread.start_new_thread(self._listen, ())

    def on_receive(self, data: str):
        print(f"client = '{self.connection_index}' received '{data}'")

    def _send(self, data: Optional[str]):
        # TODO: close connection properly on errors
        if not self.was_connected:
            print("Have not connected yet")
            return
            # raise ValueError("Have not open connection yet")
        if not data:
            raise ValueError(f"Cannot send empty data: {data}")
        outgoing = bytes(data, "UTF-8")
        self.connection.send(outgoing)
        print(f"client = '{self.connection_index}' sent '{data}'")

    def _listen(self, ):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            self.connection = c
            self.connection.connect((self.ip, self.port))
            self.was_connected = True
            self.connection_index = self.connection.recv(self.BUFSIZE).decode("UTF-8")
            print(f"client = '{self.connection_index}' listening")
            while self.is_running:
                data = self.connection.recv(self.BUFSIZE)
                if not data:
                    print("Received empty string, close connection")
                    self.is_running = False
                    break
                data = data.decode("UTF-8")
                self.on_receive(data)

#     def try_to_send(self, ):
#         while self.is_running:
#             text = input("enter text: ")
#             self._send(text)
#
#
# base_client = BaseClient()
# base_client.try_to_send()
