import socket
from threading import Thread
from tkinter import *

nickname=input('choose ur nickname')
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address='127.0.0.1'
port=8000
client.connect((ip_address,port))

print('connected with server')

class GUI:
    def _init_(self):
        self.window=Tk()
        self.window.withdraw()
        self.login=Toplevel()
        self.login.title('login')
        self.go=Button(self.login,
                       text='continue',
                       font='helvetica 14 bold',
                       command=lambda:self.goahead(self.entryname.get()))
        
def goahead(self,name):
    self.login.destroy()
    self.name=name
    rcv=Thread(target=self.receive)
    rcv.start()
def receive(self):
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message =='nickname':
                client.send(self.name.encode('utf-8'))
            else:
                pass
        except:
            print('an error occured')
            client.close()
            break
def write():
    while True:
        message ='{}:{}'.format(nickname,input(''))

receive_thread=Thread(target=receive)
receive_thread.start()
write_thread=Thread(target=write)
write_thread.start()
