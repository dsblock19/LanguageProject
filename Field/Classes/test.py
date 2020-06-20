from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion

x = StoConversion
y = WordGen


while True:
    prog = input('Program: ')
    if prog == 'WordGen':
        x.NewFam()
        print('')
    elif prog == 'Conversion':
        y.InSto()
