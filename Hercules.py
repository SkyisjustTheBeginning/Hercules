import random
import socket
OddKey = 5
import os
import psutil
from datetime import datetime
date = datetime.date(datetime.now())
batterylife = psutil.sensors_battery()
current_time = datetime.time(datetime.now())
Morning = [0,1,2,3,4,5,6,7,8,9,10,11]
Afternoon = [12,13,14,15,16,17]
if current_time in Morning:
    i = "Good Morning User "
elif current_time in Afternoon:
    i = "Good Afternoon User "
else:
    i = "Good Evening User "
def user_setup():
    R1 = [1,2,3,4,5,6,7,8,9]
    R2 = [9,6,3,5,8,1,3,0,4]
    banned = ["-","/","+","=","@",",",".","!","#","$","%","^","&","*","(",")"]
    print("""
    ████████╗███████╗██████╗░███╗░░░███╗░██████╗  ░█████╗░███╗░░██╗██████╗░
    ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔════╝  ██╔══██╗████╗░██║██╔══██╗
    ░░░██║░░░█████╗░░██████╔╝██╔████╔██║╚█████╗░  ███████║██╔██╗██║██║░░██║
    ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║░╚═══██╗  ██╔══██║██║╚████║██║░░██║
    ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██████╔╝  ██║░░██║██║░╚███║██████╔╝
    ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

    ░█████╗░░█████╗░███╗░░██╗██████╗░██╗████████╗██╗░█████╗░███╗░░██╗░██████╗
    ██╔══██╗██╔══██╗████╗░██║██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
    ██║░░╚═╝██║░░██║██╔██╗██║██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
    ██║░░██╗██║░░██║██║╚████║██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
    ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
    ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░
        """)
    print(
        """Makers of Eternity OS will not be selling any of your information to third-parties.\nWe might use the information for special user experience.\nThese credentials will be stored in your local computer , encrypted.\nThank you for using Eternity OS""")
    username = str(input("Username:"))
    gender = int(input("""Gender:
        [1] Male
        [2] Female
        [3] Rather not say
        [4] Custom\n"""))
    age = int(input("Age:"))
    country = str(input("Country(of origin):"))
    password = str(input("Password:"))
    nameforfile = username + "profile" + ".txt"
    profile = open(nameforfile, "w")
    r3code = random.choice(R1)
    r2code = random.choice(R2)
    r1code = random.choice(R1)
    r4code = str(r3code) + str(r2code) + str(r1code)
    for i in banned:
        if i in password:
            print("Banned Character Entered")
            login()
    print("Your Special R-3 Code is", r4code)
    rcredits = open("Credentials.txt", "a")
    cipher = ''
    for char in password:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + OddKey
        cipher += chr(code)
    password = cipher
    r4code = int(r4code) + 498
    rcredits.write(username + "." + str(password) + "/" + str(r4code))
    rcredits.write("\n")
    rcredits.close()
    profilecontent = "Username:" + str(username) + "\n" + "Gender:" + str(
        gender) + "\n" + "Country:" + country + "\n" + "Age:" + str(age)
    profile.write(profilecontent)
    profile.write("\n")
    profile.close()
    print("User " + username + " Has been saved")
    print("Directing to login")
    verification()
def main_os(user,password,shadowcode):
    print(""" 
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──██████─██████████████─████████████████───██████████████─██████──██████─██████─────────██████████████─██████████████─
─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██████████─██░░████████░░██───██░░██████████─██░░██──██░░██─██░░██─────────██░░██████████─██░░██████████─
─██░░██──██░░██─██░░██─────────██░░██────██░░██───██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────██░░██─────────
─██░░██████░░██─██░░██████████─██░░████████░░██───██░░██─────────██░░██──██░░██─██░░██─────────██░░██████████─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██─────────██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─██░░██████████─██░░██████░░████───██░░██─────────██░░██──██░░██─██░░██─────────██░░██████████─██████████░░██─
─██░░██──██░░██─██░░██─────────██░░██──██░░██─────██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────────────██░░██─
─██░░██──██░░██─██░░██████████─██░░██──██░░██████─██░░██████████─██░░██████░░██─██░░██████████─██░░██████████─██████████░░██─
─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████──██████─██████████████─██████──██████████─██████████████─██████████████─██████████████─██████████████─██████████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    """)
    log = open("log.txt","a")
    report = datetime.time(datetime.now())
    finalreport = str(report) + str(date) + "  User " + user + " Logged in"
    log.write(finalreport)
    log.write("\n")
    print(i + user)
    print("The Date is", date)
    print("Battery Life:", batterylife.percent)
    os.chdir(r'C:\Users\Trillion\Desktop\Hercules\DailyRead\DailyRead')
    os.system("scrapy crawl Hercule --nolog")
    os.chdir(r'C:\Users\Trillion\Desktop\Hercules')
    print('Loading up your daily read .....')
    urls = []
    with open('urls.txt','r') as handle:
        urls = handle.readlines()
    v = 1
    for read in urls:
        print('['+str(v)+'] Article : ' + read + '  ')
        v += 1
    print("""Applications:
    [1] T-9 Browser
    [2] Book Viewer
    [3] Covid-19 Tracker
    [4] Encryption Program
    [5] EternalForecast
    [6] QuantumCommand
    [7] ChatGPT Interface
    [8] Clone - In-house virtual assistant
    [9] Currency Converter
    [10] Electron Security
    [11] View System Data
    [12] Google Chrome
    [13] Neutron Note
    [14] Access Manual
    [15] Delete User Profile
    [16] Log Off""")
    app = int(input(""))
    if app == 2:
        import QuantumReader
        main_os(user,password,shadowcode)
    elif app == 1:
        import TBrowser
        main_os(user,password,shadowcode)
    elif app == 3:
        import CovidTracker
        main_os(user,password,shadowcode)
    elif app == 4:
        import Encryption
        main_os(user,password,shadowcode)
    elif app == 5:
        import EternalForecast
        main_os(user,password,shadowcode)
    elif app == 6:
        import QuantumCommand
        main_os(user,password,shadowcode)
    elif app == 7:
        import chatgpt_interface
        main_os(user,password,shadowcode)
    elif app == 8:
        import Clone
        main_os(user,password,shadowcode)
    elif app == 9:
        import Currency
        main_os(user,password,shadowcode)
    elif app == 10:
        import PasswordGene
        main_os(user,password,shadowcode)
    elif app == 11:
        hostname = socket.gethostname()
        host_ip = socket.gethostbyaddr(hostname)
        print("Username -" , user)
        print("Password -" , password)
        print("R-3 Code -" , shadowcode)
        print("IP Address -" , host_ip)
        main_os(user,password,shadowcode)
    elif app == 12:
        os.system("start chrome.exe")
        main_os(user,password,shadowcode)
    elif app == 13:
        import notepad
        main_os(user,password,shadowcode)
    elif app == 14:
        print('Manual in development.')
        main_os(user,password,shadowcode)
    elif app == 15:
        import deletion
        main_os(user,password,shadowcode)
    elif app == 16:
        report = str(datetime.time(datetime.now())) + str(date)
        log.write(report + " User " + user + " Has logged off")
        log.write("\n")
        log.close()
        verification()
def verification():
        global verified
        reader = open("Credentials.txt","r")
        print("""
            ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
            ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
            ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
            ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
            ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
            ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝""")
        x = []
        for i in reader.readlines():
            x.append(i)
        targetuser = str(input("Username:"))
        nonverified = str(input("Password:"))
        ncode = str(input("Special R-3 Code:"))
        for l in x:
            if targetuser in l:
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
                nonverified = nonverified.upper()
                if nonverified == securelink:
                    code1 = l.split("/", 2)
                    v4 = code1[1]
                    v5 = v4.split("\n", 2)
                    v5 = v5[0].split("/", 2)
                    actualcode = int(v5[0]) - 498
                    if int(actualcode) == int(ncode):
                        main_os(targetuser, securelink, ncode)
                    else:
                        print("Wrong R-3 Code")
                        verification()
                elif nonverified != securelink:
                    print("Incorrect Password")
                    verification()
print("""
██╗░░██╗███████╗██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗░██████╗
██║░░██║██╔════╝██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝██╔════╝
███████║█████╗░░██████╔╝██║░░╚═╝██║░░░██║██║░░░░░█████╗░░╚█████╗░
██╔══██║██╔══╝░░██╔══██╗██║░░██╗██║░░░██║██║░░░░░██╔══╝░░░╚═══██╗
██║░░██║███████╗██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝╚═════╝░
""")
print("""
[1] Login
[2] Setup Eternity OS""")
decision = int(input(""))
if decision == 1:
    verification()
elif decision == 2:
    user_setup()
