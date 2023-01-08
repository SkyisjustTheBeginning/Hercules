import os
import time
def deletion(target,password,r3):
    choice = input("Are you sure about this ? [Y/N]")
    if choice == "Y":
        print("Deleting User Profile.....")
        targetprofile = target + "profile" + ".txt"
        os.remove(targetprofile)
        print("User profile deleted")
        print("Deleting user from Credentials.....")
        r3 = int(r3) + 498
        stripcommand = target + "." + password + "/" + str(r3)
        with open('Credentials.txt', 'r') as fr:
            for i in fr.readlines():
                if target in i:
                    with open('Credentials.txt', 'w') as fw:
                        if i.strip("\n") != stripcommand:
                           fw.write(i)
        print("User has been deleted.")
        time.sleep(45)
reader = open("Credentials.txt","r")
print("""
██████╗░███████╗██╗░░░░░███████╗████████╗███████╗  ██╗░░░██╗░██████╗███████╗██████╗░
██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝  ██║░░░██║██╔════╝██╔════╝██╔══██╗
██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░  ██║░░░██║╚█████╗░█████╗░░██████╔╝
██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░  ██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗  ╚██████╔╝██████╔╝███████╗██║░░██║
╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝

██████╗░██████╗░░█████╗░███████╗██╗██╗░░░░░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██║░░░░░██╔════╝
██████╔╝██████╔╝██║░░██║█████╗░░██║██║░░░░░█████╗░░
██╔═══╝░██╔══██╗██║░░██║██╔══╝░░██║██║░░░░░██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██║░░░░░██║███████╗███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚══════╝""")

usertobedeleted = input("Username to be deleted:")
passwordofuser = str(input("Password of user:"))
code = int(input("R-3 Code:"))
for l in reader.readlines():
    x = l.split(".", 2)
    v1 = x[1]
    v2 = v1.split("\n", 2)
    v2 = v2[0].split("/", 2)
    securelink = v2[0]
    crypto = securelink
    text = ''
    for char in crypto:
        if not char.isalpha():
            continue
        char = char.upper()
        code2 = ord(char) - 5
        text += chr(code2)
    securelink = text
    nonverified = passwordofuser.upper()
    if nonverified == securelink:
        code1 = l.split("/", 2)
        v4 = code1[1]
        v5 = v4.split("\n", 2)
        v5 = v5[0].split("/", 2)
        actualcode = int(v5[0]) - 498
        if int(actualcode) == int(code):
            print("Access Granted")
            deletion(usertobedeleted,crypto,code)
        else:
            print("Wrong R-3 Code")

