import time, threading
import socket
import json


class Server:
    def __init__(self):
        self.host = ''
        self.port = 13580
        self.clients = []
        self.socket = None
        self.socket_thread = None
        self.get_translation = None
        self.get_yaw = None
        self.get_rotation = None
        self.set_target = None

    def Start(self):
        self.socket_thread = threading.Thread(target=self.Run)
        self.socket_thread.start()

    def Run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()

        while True:
            conn, addr = self.socket.accept()
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                target = json.loads(data.decode('UTF-8'))
                print(target)
                self.set_target(target)
                time.sleep(1/60)