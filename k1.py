import jdatetime
import os
from clint.textui import colored, puts
import requests
import urllib.request
from bs4 import BeautifulSoup
# pip install speedtest-cli
from speedtest import Speedtest
import socket
import uuid
import hashlib
import easygui
import winsound
import platform

def cowsay(say):
    import cowsay
    # cowsay.stegosaurus(say)
    cowsay.cow(say)


text = """
    ╔═══════════════════════════════════════════╗
    ║          K1 Command version 1.5           ║
    ║you can type help and see available command║
    ║           programmer K1.Adili             ║
    ║        email: k1adili@gmail.com           ║
    ╚═══════════════════════════════════════════╝
    
    Type 'help' and see available command
    """

# print("\033[1;37;40m {}".format(text))

text2 = """
    
              K1 Command version 1.5           
    you can type help and see available command
               programmer K1.Adili             
            email: k1adili@gmail.com           
    

    Type 'help' and see available command
    """

cowsay(text2)

"""
TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	30	No effect	0	Black	40
Red	31	Bold	1	Red	41
Green	32	Underline	2	Green	42
Yellow	33	Negative1	3	Yellow	43
Blue	34	Negative2	5	Blue	44
Purple	35			Purple	45
Cyan	36			Cyan	46
White	37			White	47
"""


def random_Password():
    import random
    import string
    s1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-~[]{}<>"
    password = "".join(random.sample(s1, 16))
    print("\033[1;32;40m  {}".format(password))



def temp():
    url = 'https://weather.com/weather/today/l/35.76,51.33?par=google&temp=c'
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    data = s.find_all("span",
                      class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
    txt = data[0].text.strip().replace(',', '')
    return txt

def tempMaxMin():
    url = 'https://weather.com/weather/today/l/35.76,51.33?par=google&temp=c'
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    data = s.find_all("div",
                      class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempHiLoValue--3T1DG")
    txt = data[0].text.strip().replace(',', '')
    return txt

def dollar():
    try:
        url = 'https://tejaratnews.com/قیمت-دلار'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        data = s.find_all("td", class_="")
        txt = data[1].text.strip().replace(',', '')
        # print(txt)
        return data[1].text.strip()
    except:
        print('ERROR!')

def euro():
    try:
        url = 'https://tejaratnews.com/قیمت-دلار'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        data = s.find_all("td", class_="")
        # txt = data[4].text.strip().replace(',', '')
        # print(txt)
        return data[4].text.strip()
    except:
        print('ERROR!')



def hash_def():
    file_path = easygui.fileopenbox()
    print("\033[1;32;40m file path:    {}".format(file_path))
    BLOCK_SIZE = 65536  # The size of each read from the file
    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file_path, 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file
    return file_hash.hexdigest()


def speed_test():
    try:
        print("\033[1;31;40m {}".format('Please wait ...'))
        st = Speedtest()
        do = str(round(st.download()/1000000,2))
        up = str(round(st.upload()/1000000,2))
        doMB = str(round(st.download(),2))
        doMb = str(round(st.download()/8/10000,2))
        upMB = str(round(st.upload(),2))
        upMb = str(round(st.upload()/8/10000,2))
        # do = str(st.download())
        # up = str(st.upload())
        # print("\033[1;32;40m Download: {} Mb/s".format(do/1000000/8))
        print("\033[1;32;40m Download: {} MB/s".format(doMB))
        print("\033[1;32;40m Download: {} Mb/s".format(doMb))
        # print("\033[1;321;40m Upload: {} Mb/s".format(up/1000000/8))
        print("\033[1;321;40m Upload: {} MB/s".format(upMB))
        print("\033[1;321;40m Upload: {} Mb/s".format(upMb))
        st.get_servers([])
        pi = str(st.results.ping)
        print("\033[1;321;40m Ping: {}".format(pi))
    except:
        print("\033[1;321;40m Ping: {}".format('check your internet connection'))


def getip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except:
        pass


def isp():
    try:
        url = 'https://www.whoismyisp.org'
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        data = s.find_all("p", class_="isp")
        txt = data[0].text.strip().replace(',', '')
        return txt
    except:
        puts(colored.red('Internet is disconected'))


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


def run():
    # text = """
    #
    # Type 'help' and see available command
    # """
    print("\033[1;37;40m {}".format(""))

    a = input('>_ ')


    if a.lower() == 'help':

        helpText = """
        ╔══════════════════════════════════════════╗
        ║..........................................║
        ║time        show jalali date and time.    ║
        ║folder      create folder with date name. ║
        ║internet    check your internet conection.║
        ║isp         show your internet isp name.  ║
        ║ip          show your local ip and wan ip.║
        ║guid        generate GUID or UUID.        ║
        ║filehash    show file hash.               ║
        ║proxykill   Disable yore proxy server.    ║
        ║fdns        Flushdns.                     ║
        ║ping        ping google.com               ║
        ║$           Show Dollar price vs Toman.   ║
        ║eu          Show Euro price vs Toman.     ║
        ║os          Show system information.      ║
        ║temp        Show Tehran temperature.      ║
        ║rp          Generate random password.     ║
        ║cowsay      Create cowsay text.           ║
        ║..........................................║
        ╚══════════════════════════════════════════╝
        """
        print("\033[1;33;40m {}".format(helpText))
        # puts(colored.yellow(helpText))
    elif a.lower() == 'time':
        # puts(colored.cyan(str(jdatetime.datetime.now())))
        print("\033[1;32;40m {}".format(str(jdatetime.datetime.now())))
    elif a.lower() == 'folder':
        persianDate = jdatetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\\' + persianDate)
        os.makedirs(path)
        text = 'folder created in desktop and name is {}'.format(persianDate)
        print("\033[1;32;40m {}".format(text))

    elif a.lower() == 'internet':
        if connect():
            print("\033[1;32;40m {}".format('Internet is conected'))
        else:
            print("\033[1;31;40m {}".format('Internet is disconected'))
    elif a.lower() == 'isp':
        print('\033[1;35;40m please wait...', end="\r")
        ispStr = isp()
        print("\033[1;32;40m {}".format(ispStr))

    elif a.lower() == 'ip':
        print("\033[1;32;40m local ip:  {}".format(str(socket.gethostbyname(socket.gethostname()))))
        print('\033[1;35;40m please wait...', end="\r")
        wanip = getip()
        print("\033[1;32;40m wan ip:    {}".format(wanip))
    elif a.lower() == 'guid':
        print("\033[1;32;40m  {}".format(str(uuid.uuid4())))

    elif a.lower() == 'proxykill':
        os.system('cmd /C "reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f"')
        print("\033[1;32;40m Proxy server disable")

    elif a.lower() == 'filehash':
        HASH = hash_def()
        print("\033[1;32;40m File hash:    {}".format(HASH))

    elif a.lower() == 'os':
        print(f"\033[1;32;40m Os: {platform.system()}")
        print(f"\033[1;32;40m Version: {platform.platform()}")
        print(f"\033[1;32;40m PC Name: {platform.node()}")
        print(f"\033[1;32;40m Processor: {platform.processor()}")

    elif a.lower() == 'fdns':
        os.system('cmd /C "ipconfig /flushdns"')
        print("\033[1;32;40m flushed the DNS")
    elif a.lower() == 'ping':
        os.system('cmd /C "ping google.com"')

    elif a.lower() == 'beep':
        frequency = 15000
        duration = 5000
        winsound.Beep(frequency, duration)

    elif a.lower() == '$':
        print('\033[1;35;40m please wait...', end="\r")
        a = dollar()
        print(f"\033[1;32;40m $: {a} Toman")
    elif a.lower() == 'eu':
        print('\033[1;35;40m please wait...', end="\r")
        eu = euro()
        print(f"\033[1;32;40m €: {eu} Toman")

    elif a.lower() == 'speedtest':
        speed_test()

    elif a.lower() == 'temp':
        print('\033[1;35;40m please wait...', end="\r")
        tem = temp()
        print(f"\033[1;32;40m Tehran temperature: {tem}ͨ")
        # print('Tehran temperature: ', tem, 'ͨ')
        maxmin = tempMaxMin()
        print(f"\033[1;32;40m Tehran Max/Min temperature: {maxmin}ͨ")
    elif a.lower() == 'rp':
        random_Password()

    elif a.lower() == 'cowsay':
        cowtext = input('enter your text: ')
        cowsay(cowtext)

    elif a.lower() == 'test':
        puts(colored.yellow(a))
        puts(colored.cyan('Kayvan Adili'))

    else:
        puts(colored.red('wrong command'))


if __name__ == '__main__':
    while True:
        run()
