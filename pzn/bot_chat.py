import re
import random

# Salutations
sapaan = ["Hai juga", "halo juga", "apaan tod", "apa kabar"]
# Insults
kerad = [f"mohon untuk menggunakan kata sopan","biasakan bilang assalammu alaikum(kalo islam)"]
# Greetings
islam = ["waalaikum salam"] 

# Introduce chatbot
print("Halo perkenalkan Saya chat bot sederhana yang dibuat oleh @ftrrahmanzk")

# Ask for user's name
print("Silahkan masukkan nama Anda:")
nama_user = input()

# Greet user
print(f"Halo {nama_user}, selamat mencoba chat bot sederhana ini")

# Start chat loop
while True:
    # Ask for user input
    x = input(f"{nama_user}\t: ")
    
    # Check for salutations
    if re.findall(r'halo|hai|apa', x) :
        print("bot_chat\t:", random.choice(sapaan),"\n")
        
    # Check for greetings
    elif re.findall(r'salam|alaikum|assalammu alaikum', x) :
        print("bot_chat\t:", random.choice(islam),"\n")
        
    # Check for insults
    elif re.findall(r'kontol|memek|m3m3m|yatim', x) :
        print("bot_chat\t:", random.choice(kerad),"\n")
        
    # Exit chat loop
    elif x.lower() in ["break", "exit"]:
        break
        
    # Default response
    else:
        print("bot_chat\t: Maaf, saya belum sempurna untuk menjawab pertanyaan Anda.\n")
