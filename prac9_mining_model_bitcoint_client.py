#pip install bitcoinlib

from bitcoinlib.wallets import Wallet
w = Wallet.create('Wallet1')
key1 = w.get_key()
print('Wallet Address:',key1.address)
w.scan()
print(w.info())
