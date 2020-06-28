from MultiFamWordGenInky import WordGen
from StoConversion import StoConversion
from StoLog import StoLog
from CustomWordGenInky import CustWordGen
from ConjugateVerb import ConjugateVerb
#from AddWord import Add2Dic
from LookupWord import LookUp

x = StoConversion()
y = WordGen()
z = StoLog()
a = CustWordGen()
b = ConjugateVerb()
#c = Add2Dic()
d = Lookup()


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
    #elif prog == 'ADD WORD':
        #c.AddWord()
    elif prog == 'LOOKUP':
        d.WordDef()
