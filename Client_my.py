import socket
import threading

nickname = input("Введите ваш nikename: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('46.149.77.240', 5555))

def recieving():
    while True:
        try:
            message = client.recv(102400).decode('asci')
            if message == 'NICK':
                client.send(nickname.encode('asce'))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('asci'))
receive_thread = threading.Thread(target=recieve)

