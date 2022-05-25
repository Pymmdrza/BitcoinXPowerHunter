import threading
import time
import sys
from rich.console import Console

from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hexer import mHash
import multiprocessing

console = Console()

mmdrza = '''
                    ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
                    ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
                    ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
                    ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
                    ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
                    ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                  ||======================================================||
                  ||===========  ╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗  ===========||
                  ||===========  ║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║  ===========||
                  ||===========  ╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩  ===========||                                                                                                                            
                  ||------------------------------------------------------||
                  ||- WebSite ------------------------------- Mmdrza.Com -||
                  ||- MAIL    ---------------------------- X4@Mmdrza.Com -||
                  ||- DEV     ---------------------------- DEV.to/Mmdrza -||
                  ||- GiTHUB  ---------------------- Github.Com/PyMmdrza -||
                  ||- MEDIUM  -------------- PythonWithMmdrza.Medium.Com -||
                  ||======================================================||
'''

filename = 'btc500.txt'
with open(filename) as f:
	add = f.read().split()
add = set(add)
z = 1


def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)


delay_print('\n\n\n\n\n\n\n\nCan You Download Rich Wallet List For This Program Follow GitHub.Com/PyMmdrza Or Mmdrza.Com')
console.clear()
console.print('[gold1]' + str(mmdrza) + '[/]')


def mmdrza():
	z = 0
	w = 0
	
	while True:
		hex64 = mHash()
		PRIVATE_KEY: str = hex64
		hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
		hdwallet.from_private_key(private_key=PRIVATE_KEY)
		priv = hdwallet.private_key()
		p2pkh = hdwallet.p2pkh_address()
		p2sh = hdwallet.p2sh_address()
		p2wpkh = hdwallet.p2wpkh_address()
		p2wsh = hdwallet.p2wsh_address()
		p2wpkh2 = hdwallet.p2wpkh_in_p2sh_address()
		p2wsh2 = hdwallet.p2wsh_in_p2sh_address()
		if p2pkh in add or p2sh in add or p2wsh in add or p2wpkh in add or p2wsh2 in add or p2wpkh2 in add:
			f = open("BtcWalletWinner.txt", "a")
			f.write('\nAddress         :  ' + str(p2pkh))
			f.write('\nAddress         :  ' + str(p2sh))
			f.write('\nAddress         :  ' + str(p2wpkh))
			f.write('\nAddress         :  ' + str(p2wsh))
			f.write('\nAddress         :  ' + str(p2wpkh2))
			f.write('\nAddress         :  ' + str(p2wsh2))
			f.write('\nPrivateKey      :  ' + str(priv))
			f.close()
			w += 1
		else:
			console.print('[gold1] --- P2PKH([red1]' + str(z) + '[/][gold1]) --- P2WPKH([/][red1]' + str(z) + '[/][gold1])  --- P2WPKH in P2SH([red1]' + str(z) + '[/][gold1]) --- P2SH([/][red1]' + str(z) + '[/][gold1]) --- P2WSH([/][red1]' + str(z) + '[/][gold1])', end="\r")
			z += 1
mmdrza()

t = threading.Thread(target=mmdrza)
t.start()
