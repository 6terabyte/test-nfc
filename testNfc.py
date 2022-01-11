#import socket
import binascii
import nfc

#class Client:
#  def __init__(self, socket_path):
#      self.socket_path = socket_path
#
#  def send(self, num):
#    s = self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#    s.connect(self.socket_path)
#    message = num
#    s.send(message.encode())
#    data = s.recv(1024)
#    s.close()
#
#def send(num):
#  client = Client('/tmp/nfcTest.sock')
#  client.send(num)

def on_connect(tag):
  idm = binascii.hexlify(tag._nfcid)
  print(str(idm))
  #send(str(idm))

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': on_connect})
clf.close()
