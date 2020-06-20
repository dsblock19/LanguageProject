from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion

x = StoConversion
y = WordGen


while True:
    prog = input('Program: ')
    if prog == 'WordGen':
        y.NewFam()
        print('')
    elif prog == 'Conversion':
        x.InSto()
