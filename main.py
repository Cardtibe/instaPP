import time
import os
import urllib.request
import requests 
from bs4 import BeautifulSoup
dosya = open(os.getcwd()+"/"+"Fkrta.txt", "w")
API_ENDPOINT = "https://izuum.com/index.php"
print('''
   _____              _ _______ _ _            _____  _____  
  / ____|            | |__   __(_) |          |  __ \|  __ \ 
 | |     __ _ _ __ __| |  | |   _| |__   ___  | |__) | |__) |
 | |    / _` | '__/ _` |  | |  | | '_ \ / _ \ |  ___/|  ___/ 
 | |___| (_| | | | (_| |  | |  | | |_) |  __/ | |    | |     
  \_____\__,_|_|  \__,_|  |_|  |_|_.__/ \___| |_|    |_|                                                                                                                            
''')
nick=(input("Enter victim instagram name: ")) 
data = {'submit':nick}
con=input("Enter file name:  ") 
  
r = requests.post(url = API_ENDPOINT, data = data) 
  
paste = r.text
dosya.write(paste) 
dosya = open(os.getcwd()+"/"+"Fkrta.txt", "r")
for i in range(0,381):
	dosya.readline()
sn=dosya.readline()
pt=""
for i in sn:
	if i=="'":
		break
	else:
		pt+=i
sn=pt.replace("amp;","")
urllib.request.urlretrieve(sn, os.getcwd()+"/"+con+".jpg")
os.remove("Fkrta.txt")
print("\n Contact  GitHub CardTibe -- İnstagram CardTibe")
