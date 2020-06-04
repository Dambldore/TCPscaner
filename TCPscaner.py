import socket
from contextlib import closing
import threading

ips = []

with open("config.txt") as f:
    ips = list(f.readline().split(","))
    for i in range(len(ips)):
        ips[i] = ips[i].replace("\n", "")
        ips[i] = ips[i].replace(" ", "")


def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        with closing(s.connect((ip, port))):
            print("Port №", port, "is open")
    except Exception:
        pass


for ip in ips:
    print("Checking ports " + ip)
    for port in range(4000):
        thread = threading.Thread(target=check_port, args=(ip, port))
        thread.start()
        thread.join()
