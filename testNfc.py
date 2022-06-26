#import socket
import binascii
import nfc

def connect(tag):
  idm = binascii.hexlify(tag._nfcid)
  print(str(idm))

clf = nfc.ContactlessFrontend('usb')
clf.sense(nfc.clf.RemoteTarget("212F"))
clf.connect(rdwr={'targets': ['212F', '424F'], 'on-connect': connect})
clf.close()
