import re
import random

print("Halo perkenalkan Saya chat bot sederhana")

print("yang dibuat oleh @ftrrahmanzk")

print("silahkan masukkan nama anda")
nama_user = input()

print(f"Halo {nama_user} selamat mencoba bot_chat sederhana ini")



sapaan = ["Hai juga", "halo juga", "apaan tod",f"apa {nama_user}" ]
kerad = [f"mohon untuk menggunakan kata sopan","biasakan bilang assalammu alaikum(kalo islam)"]
islam = [f"waalaikum salam, {nama_user}"] 

while True:
    x = input(f"{nama_user}\t: ")
    if re.findall(r'halo|hai|apa', x) :
        print("bot_chat\t:", random.choice(sapaan),"\n")
        
    if re.findall(r'salam|alaikum|assalammu alaikum', x) :
        print("bot_chat\t:", random.choice(islam),"\n")
        
    if re.findall(r'kontol|meme|m3m3m|yatim', x) :
        print("bot_chat\t:", random.choice(kerad),"\n")
        
    #   """bug di chat bot malah chat else juga muncul"""
      
    else:
        print("bot_chat\t:maaf bot ini belum sempurna untuk bahan gabutmu\n")
        
        
