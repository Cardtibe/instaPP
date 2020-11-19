import time
import os
import urllib.request
import requests
from bs4 import BeautifulSoup
print('''
   _____              _ _______ _ _            _____  _____  
  / ____|            | |__   __(_) |          |  __ \|  __ \ 
 | |     __ _ _ __ __| |  | |   _| |__   ___  | |__) | |__) |
 | |    / _` | '__/ _` |  | |  | | '_ \ / _ \ |  ___/|  ___/ 
 | |___| (_| | | | (_| |  | |  | | |_) |  __/ | |    | |     
  \_____\__,_|_|  \__,_|  |_|  |_|_.__/ \___| |_|    |_|                                                                                                                            
''')
link = "https://izuum.com/index.php"
#nick= input("Enter instagram nick: ")
nick="xta.txt"
def ppd(n,x):
	dosya=open(os.getcwd()+"/"+"Fkrt.txt","w")
	r = requests.post(url=link, data={'submit':n})
	paste= r.text
	dosya.write(paste)
	dosya=open(os.getcwd()+"/"+"Fkrt.txt","r")
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
	print(sn)
	urllib.request.urlretrieve(sn, os.getcwd()+"/nres/"+str(x)+".jpg")
	os.remove("Fkrt.txt")
	dosya.close()
rn=8
if "txt" in nick:
	while True:
		rn+=1
		try:
			nlis=open(os.getcwd()+"/"+nick,"r")		
			ppd(nlis.readline(),rn)
		except:
			print("hata")
			break
else:
	cnt=input("Enter file name: ")
	ppd(nick,cnt)
print("\n Contact  GitHub CardTibe -- İnstagram CardTibe")

	
