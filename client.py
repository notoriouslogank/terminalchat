import random
import socket
from datetime import datetime
from threading import Thread

from colorama import Fore, init
from rich import print as pprint

init()
colors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
]

client_color = random.choice(colors)
SERVER_HOST = input("IP to connect to: ")
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
pprint(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
name = input("Username: ")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input(f"\n")
    if to_send.lower() == "q":
        break
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_send = (
        f"[{date_now}] {client_color}{name}{Fore.RESET}{separator_token}{to_send}\n"
    )
    s.send(to_send.encode())

s.close()
