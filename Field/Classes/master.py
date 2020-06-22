from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion
from StoLog import StoLog

x = StoConversion
y = WordGen
z = StoLog


while True:
    prog = input('Program: ')
    if prog == 'WordGen':
        y.NewFam()
        print('')
    elif prog == 'Conversion':
        x.InSto()
    elif prog == 'Log':
        z.StoLog()
