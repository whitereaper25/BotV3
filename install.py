import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("""
      ██████╗░░█████╗░██████╗░██╗░░██╗
      ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
      ██║░░██║███████║██████╔╝█████═╝░
      ██║░░██║██╔══██║██╔══██╗██╔═██╗░
      ██████╔╝██║░░██║██║░░██║██║░╚██╗
      ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
      ██████╗░░█████╗░████████╗
      ██╔══██╗██╔══██╗╚══██╔══╝
      ██████╦╝██║░░██║░░░██║░░░
      ██╔══██╗██║░░██║░░░██║░░░
      ██████╦╝╚█████╔╝░░░██║░░░
      ╚═════╝░░╚════╝░░░░╚═╝░░░
      ░ ░\x1b[00m\033[041m TERMUX WHATSAPP BOT MrDevils  \033[00m\x1b[1;00m░░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░\x1b[00m
""")
m('\x1b[00m\033[041m Install bahan automatis  \033[00m')
m('\x1b[00m\033[041m Jangan Keluar Dari Termux Sebelum Selesai Menginstall!!  \033[00m')
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install nano")
os.system("pkg install python -y")
os.system("pkg install python2 -y")
os.system("pkg install nodejs -y")
os.system("pkg install libwebp -y")
os.system("pkg install ffmpeg -y")
os.system("pkg install wget -y")
os.system("pkg install tesseract -y")
os.system("bash install.sh")
os.system("npm install --dev")
os.system("npm i imgbb-uploader")
m('\x1b[00m\033[041m Memulai Whatsapp Bot...  \033[00m')
os.system("clear")
os.system("node index")
m("DONE")