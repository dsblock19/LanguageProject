from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion
from StoLog import StoLog
from CustomWordGenInky import CustWordGen

x = StoConversion()
y = WordGen()
z = StoLog()
a = CustWordGen()


while True:
    prog = input('Program: ')
    prog = prog.upper()
    if prog == 'WORDGEN':
        y.NewFam()
    elif prog == 'CONVERSION':
        x.InSto()
    elif prog == 'LOG':
        z.StoLog()
    elif prog == 'CUSTOM WORDGEN':
        a.CustNewFam()
