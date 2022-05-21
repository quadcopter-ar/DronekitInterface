import time, threading
import socket
import json


class Server:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 13580
        self.clients = []
        self.socket = None
        self.socket_thread = None
        self.get_translation = None
        self.get_yaw = None
        self.get_rotation = None
        self.set_target = None
        self.prev_status = 0

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
                data = conn.recv(76)
                if not data:
                    break
                try:
                    check_str = data.decode("UTF-8")
                    check_str = list(check_str.split("{"))
                    
                    # print(check_str)
                    # print(check_str)
                    check_str = check_str[1:-1]
                    
                    if(len(check_str)>0):
                        check_string = check_str[0]
                        target = json.loads("{" + check_string)
                        print(target)
                        # print(target)
                        target['status'] = int(target['status'])
                        if self.prev_status != target['status']:
                            print("Status change from", self.prev_status, 'to', target['status'])
                            
                            self.prev_status = target['status']

                        
                        target['x'] = float(target['x'])
                        target['y'] = float(target['y'])
                        target['z'] = float(target['z'])
                        target['yaw'] = float(target['yaw'])

                        self.set_target(target)

                except json.JSONDecodeError as e:
                    print("Couldn't decode JSON: ", e, data.decode('UTF-8'))