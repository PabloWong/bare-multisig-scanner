#|/usr/bin/python3

from bitcoinrpc.authproxy import AuthServiceProxy

with open("/hdd/.bitcoin/.cookie","r") as f:
    cookie = f.read()
cookie = cookie.split(":")
access = AuthServiceProxy("http://{}:{}@127.0.0.1:8332".format(cookie[0],cookie[1]),timeout=300)
blocks = access.getblockcount()
blockhash = blockhash=access.getblockhash(1)
block = access.getblock(blockhash)

txs=[]
for i in range(1,blocks):
    block = access.getblock(block['nextblockhash'],2)
    for tx in block['tx']:
        for vout in tx['vout']:
            try: txtype = vout['scriptPubKey']['type']
            except: txtype =False

            try: addresslen= len(vout['scriptPubKey']['addresses'])
            except: addresslen = 0

            if txtype == 'multisig':
                print("{}|{}|{}".format(txtype, i, tx['txid']))
            if  addresslen > 1:
                print("{}|{}|{}".format(addresslen,i, tx['txid'],txtype)   )
            
            if (txtype=='multisig'  or addresslen > 1) and not(txtype=='multisig'  and addresslen > 1):
                print(':ISIDORO:',addresslen, i, txtype, tx['txid'])

