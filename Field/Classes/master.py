from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion
from StoLog import StoLog
from CustomWordGenInky import CustWordGen
from ConjugateVerb import ConjugateVerb

x = StoConversion()
y = WordGen()
z = StoLog()
a = CustWordGen()
b = ConjugateVerb()


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
    elif prog == 'CONJUGATE':
        b.Conjugate()
