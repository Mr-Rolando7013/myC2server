#Chapter2
import socket

def listener_handler():
    sock.bind((host_ip, host_port))
    print("[+] Awaiting connection from client...")
    sock.listen()
    remote_target, remote_ip = sock.accept()

    # Remote_ip returns a tupple of the IP and the Port, so if you use remote_ip[0], only the ip will be returned.
    print(f'[+] Connection reveived from {remote_ip[0]}')
    remote_target.close()


host_ip = '127.0.0.1'
host_port = 2222
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener_handler()