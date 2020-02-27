import json,re,sys,os
import argparse
from time import sleep
import time
a=time.localtime()
hr=a.tm_hour
mn=a.tm_min
sc=a.tm_sec
xtime=('{}:{}:{}'.format(hr,mn,sc))
try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
   cyan = Style.BRIGHT+Fore.CYAN
   cyan2 = Style.NORMAL+Fore.CYAN
   des = Style.BRIGHT+Fore.GREEN+"『🔥』"
   kur1 = Style.BRIGHT+Fore.RED+"["
   kur2 = Style.BRIGHT+Fore.RED+"]"
except:
   print ("Please Install Modul Colorama!!\n\n\n")
   sys.exit()

try:
   import requests
   from bs4 import BeautifulSoup
except:
   print ("Please Install Modul Requests & BS4\n\n\n")
   sys.exit()

from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError

parser = argparse.ArgumentParser(description='This Scipt AllTeleBot Free.\nThis Script Not For Sale!!')
parser.add_argument(
    '-p','--phone',
    help='Enter Your Phone Number.\nExemple +6285*********',required=True
)
parser.add_argument(
    '-c','--channel',
    help='Enter Your Channel Currency.\nExample Doge,LTC,BTC,BCH,ZEC',required=True
)
argument = parser.parse_args()


banner = des+des+des+des+des+des+des+des+des+des+"""
"""+Style.BRIGHT+Fore.CYAN+"""    .___               .___       ____   ____.___.___.___.
  __| _/____  ____   __| _/____   \   \ /   /|   |   |   |
 / __ |/ ___\/  _ \ / __ |/ __ \   \   Y   / |   |   |   |
/ /_/ \  \__(  <_> ) /_/ \  ___/    \     /  |   |   |   |
\____ |\___  >____/\____ |\___  >    \___/   |___|___|___|
     \/    \/           \/    \/"""+kur1+Style.RESET_ALL+Style.BRIGHT+Fore.CYAN+""" BOT AUTO VISIT CLICKBOT """+kur2+Style.RESET_ALL+"""
    Salam Damai Tuyuler Indonesia!!!
"""+des+des+des+des+des+des+des+des+des+des+"""
"""+Style.BRIGHT+Fore.CYAN+"""Recode By   """+Style.DIM+Fore.WHITE+""" :"""+Style.RESET_ALL+""" Mc. Queen
"""+Style.BRIGHT+Fore.CYAN+"""Group Tele"""+Style.DIM+Fore.WHITE+"""   : """+Style.RESET_ALL+"""t.me/jancokkau990"""

if not os.path.exists("session"):
    os.makedirs("session")


def login(nomor):
  global client
  api_id = 717425
  api_hash = '322526d2c3350b1d3530de327cf08c07'
  phone_number = nomor

  client = TelegramClient("session/"+phone_number, api_id, api_hash)
  client.connect()
  if not client.is_user_authorized():
    try:
      client.send_code_request(phone_number)
      me = client.sign_in(phone_number, input('\n\n\n\033[1;0mEnter Yout Code : '))
    except SessionPasswordNeededError:
      passw = input("\033[1;0mYour 2fa Password : ")
      me = client.start(phone_number,passw)
  myself = client.get_me()
  os.system("clear")
  print (banner)
  print (f"{cyan}Telegram Number{res}",nomor)
  print (f"{cyan}Welcome To TeleBot{res}",myself.first_name,f"\n{cyan}This Bot Is Free!! Not For Sale!!\n\n")

def filter(channel):
   global channel_username
   global channel_entity
   global jumlah_wd
   global wallet
   if "Doge" in channel or "DOGE" in channel or "doge" in channel:
       channel_entity=client.get_entity("@Dogecoin_click_bot")
       channel_username="@Dogecoin_click_bot"
       jumlah_wd = float(obj["DOGE"]["Amount"])
       wallet = obj["DOGE"]["Address"]
   elif "LTC" in channel or "ltc" in channel:
       channel_entity=client.get_entity("@Litecoin_click_bot")
       channel_username="@Litecoin_click_bot"
       jumlah_wd = float(obj["LTC"]["Amount"])
       wallet = obj["LTC"]["Address"]
   elif "BCH" in channel or "bch" in channel:
       channel_entity=client.get_entity("@BCH_clickbot")
       channel_username="@BCH_clickbot"
       jumlah_wd = float(obj["BCH"]["Amount"])
       wallet = obj["BCH"]["Address"]
   elif "zec" in channel or "ZEC" in channel or "Zec" in channel:
       channel_entity=client.get_entity("@Zcash_click_bot")
       channel_username="@Zcash_click_bot"
       jumlah_wd = float(obj["ZEC"]["Amount"])
       wallet = obj["ZEC"]["Address"]
   elif "BTC" in channel or "btc" in channel:
       channel_entity=client.get_entity("@BitcoinClick_bot")
       channel_username="@BitcoinClick_bot"
       jumlah_wd = float(obj["BTC"]["Amount"])
       wallet = obj["BTC"]["Address"]
   else:
       print (f"{abu2}[{yellow2}Waiting!{abu2}]{yellow} Please Check Your Command\n")
       sys.exit()


def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}|{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}-{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}|{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}-{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
       sys.stdout.write("\r")
       sys.stdout.write("{}[{}\{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,cyan))
       sys.stdout.flush()
       sleep(0.125)
    sys.stdout.write("\r                                                 \r")
    sys.stdout.write(f"\r{abu2}[{yellow2}Waiting!{abu2}] {hijau}Getting Reward")


with open('Wallet.json', 'r') as myfile:
      data=myfile.read()
# parse file
obj = json.loads(data)

ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
c = requests.session()
try:
 login(argument.phone)
 filter(argument.channel)
 for i in range(5000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write(f"\r{abu2}[{yellow2}Waiting!{abu2}]{yellow} Try To Get Url Ads")
  sys.stdout.flush()
  client.send_message(entity=channel_entity,message="🖥 Visit sites")
  sleep(3)
  posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
  if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
     print (f"\n{abu2}[{red2}{xtime}{abu2}] {red}Sorry, there are no new ads available!!")
     client.send_message(entity=channel_entity,message="💰 Balance")
     sleep(5)
     posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
     message = posts.messages[0].message
     print (f"\r{abu2}[{cyan2}{xtime}{abu2}]{cyan} "+message)
     if "Available balance" in message:
        sys.stdout.write("\r                                            \r")
        jum = re.findall( r'([\d.]*\d+)', message)
        if float(jum[0]) > jumlah_wd:
           client.send_message(entity=channel_entity,message="💵 Withdraw")
           sleep(1)
           client.send_message(entity=channel_entity,message=wallet)
           sleep(1)
           client.send_message(entity=channel_entity,message=jum[0])
           sleep(1)
           client.send_message(entity=channel_entity,message="✅ Confirm")
           print (f"\r{abu2}[{cyan2}{xtime}{abu2}]{cyan} Success Withdraw",jum[0],channel_username)
        else:
           sys.exit()
     sys.exit()
  else:
    try:
     url = posts.messages[0].reply_markup.rows[0].buttons[0].url
     sys.stdout.write("\r")
     sys.stdout.write(f"\r{abu2}[{yellow2}Waiting!{abu2}]{yellow} Visit "+url)
     sys.stdout.flush()
     id = posts.messages[0].id
     r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
     soup = BeautifulSoup(r.content,"html.parser")
     if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
        sleep(2)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write(f"\r{abu2}[{cyan2}{xtime}{abu2}]{cyan} "+messageres+"\n")
        else:
           continue


     elif soup.find('div', id="headbar") is not None:
        for dat in soup.find_all('div',class_="container-fluid"):
            code = dat.get('data-code')
            timer = dat.get('data-timer')
            tokena = dat.get('data-token')
            tunggu(int(timer))
            r = c.post("https://dogeclick.com/reward",data={"code":code,"token":tokena}, headers=ua, timeout=15, allow_redirects=True)
            js = json.loads(r.text)
            sys.stdout.write(f"\r{abu2}[{cyan2}{xtime}{abu2}]{cyan} You earned "+js['reward']+" "+argument.channel+" for visiting a site!\n")
     else:
        sys.stdout.write("\r")
        sys.stdout.write("                                                                ")
        sys.stdout.write("\r")
        sys.stdout.write(f"\r{abu2}[{yellow2}Waiting!{abu2}]{yellow} Captcha Detected")
        sys.stdout.flush()
        sleep(2)
        client(GetBotCallbackAnswerRequest(
        channel_username,
        id,
        data=posts.messages[0].reply_markup.rows[1].buttons[1].data
        ))
        sys.stdout.write(f"\r{abu2}[{red2}{xtime}{abu2}] {red}Skip Captcha...!       \n")
        sleep(2)
    except KeyboardInterrupt:
         print (f"\n{abu2}[{red2}{xtime}{abu2}] {red}Exit...!")
         sleep(1)
         sys.exit()
    except:
        sleep(3)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write(f"\r{abu2}[{cyan2}{xtime}{abu2}]{cyan} "+messageres+"\n")
        else:
           pass

finally:
   client.disconnect()

