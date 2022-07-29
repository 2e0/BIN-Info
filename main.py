

import pystyle
from pystyle import *
import requests
import httpx
import os
import json
import time

while True:

	os.system('clear')


	banner = '''
	
	__________.___ _______            .___        _____       
	\______   \   |\      \           |   | _____/ ____\____  
	 |    |  _/   |/   |   \   ______ |   |/    \   __\/  _ \ 
	 |    |   \   /    |    \ /_____/ |   |   |  \  | (  <_> )
	 |______  /___\____|__  /         |___|___|  /__|  \____/ 
	        \/            \/                   \/             
	 ‎
	 ‎
	 ‎
	'''

	print(Colorate.Horizontal(Colors.white_to_red, banner, 3))

	time.sleep(2)

	bin = input(Colorate.Horizontal(Colors.white_to_red, "Veuillez mettre le BIN (ex. 456091): ", 3))

	os.system('clear')

	print(Colorate.Horizontal(Colors.white_to_red, banner, 3))


	r = httpx.get('https://api.bintable.com/v1/' + bin +'?api_key=16c70e495c68f62bd183286f7ca36643c2ed539a')

	bin_checked = json.loads(r.text)

	with open("bin_checked.json", "w") as write_file:
		json.dump(r.text, write_file)

	print(Colorate.Horizontal(Colors.white_to_red, "Scheme Card : " + bin_checked['data']['card']['scheme'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Type : " + bin_checked['data']['card']['type'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Category : " + bin_checked['data']['card']['category'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "CVV Len : " + str(bin_checked['data']['card']['cvvlen']), 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Pays : " + bin_checked['data']['country']['name'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Banque : " + bin_checked['data']['bank']['name'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Site : " + bin_checked['data']['bank']['website'], 3))
	print(Colorate.Horizontal(Colors.white_to_red, "Allo : " + bin_checked['data']['bank']['phone'], 3))

	print('\n')
	print('\n')
	print('\n')

	restart = input(Colorate.Horizontal(Colors.white_to_red, "Voudrais-tu recommancer ? (y/n) :", 3))

	if(restart == "y"):
		continue
	elif(restart == "n"):
		break













