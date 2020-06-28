from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion
from StoLog import StoLog

x = StoConversion
y = WordGen
z = StoLog


while True:
    prog = input('Program: ')
    prog = prog.upper()
    if prog == 'WORDGEN':
        y.NewFam()
        print('')
    elif prog == 'CONVERSION':
        x.InSto()
    elif prog == 'LOG':
        z.StoLog()
