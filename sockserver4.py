#Chapter 4
import socket

def listener_handler():
    sock.bind((host_ip, host_port))
    print("[+] Awaiting connection from client...")
    sock.listen()
    remote_target, remote_ip = sock.accept()

    # Remote_ip returns a tupple of the IP and the Port, so if you use remote_ip[0], only the ip will be returned.
    print(f'[+] Connection reveived from {remote_ip[0]}')
    while True:
        try:
            message = input('Message to send#> ')
            if message == 'exit':
                remote_target.send(message.encode())
                remote_target.close()
                break
            # Send message to the client
            remote_target.send(message.encode())
            # Receive messaage from the client.
            response = remote_target.recv(1024).decode()
            if response == 'exit':
                print('[-] The client has terminated the session.')
                remote_target.close()
                break
            print(response)
        except KeyboardInterrupt:
            print('[+] Keyboard interrupt issued.')
            remote_target.close()
            break

        except Exception:
            remote_target.close()
            break

host_ip = '127.0.0.1'
host_port = 2222
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener_handler()