import os
print("""
░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ██████╗░███████╗░█████╗░██████╗░███████╗██████╗░
██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ██████╔╝█████╗░░███████║██║░░██║█████╗░░██████╔╝
╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ██╔══██╗██╔══╝░░██╔══██║██║░░██║██╔══╝░░██╔══██╗
░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██║░░██║███████╗██║░░██║██████╔╝███████╗██║░░██║
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝""")
book_reader = open("books.txt","r")
print("""Choices:
[1] Artemis Fowl
[2] Artemis Fowl : The Arctic Incident
[3] Artemis Fowl : The Eternity Code
[4] The Spy - Clive Cussler
[5] The Wrecker - Clive Cussler
[6] Diary of a Wimpy Kid - Rodrick Rules
[7] Percy Jackson and the Olympians - Sea of Monsters
[8] Percy Jackson - The Titan's Curse""")
choice = str(input(""))
for i in book_reader.readlines():
    if choice in i:
        split1 = i.split("-",2)
        os.system("start " + split1[1])