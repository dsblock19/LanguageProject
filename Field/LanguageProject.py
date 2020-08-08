import master

x = master.SQLint()
y = master.WordCreation()
z = master.inkyOnly()


while True:
    prog = input('Program: ')
    prog = prog.upper()

    if prog == 'ADD WORD':
        x.AddWord()
    elif prog == 'LOOKUP' or prog == 'STO':
        x.WordDef()
    elif prog == 'LOOKUP ENGLISH' or prog == 'ENGLISH':
        x.WordDefEng()
    elif prog == 'PART OF SPEECH' or prog == 'POS':
        x.PartOfSpeech()
    elif prog == 'CUSTOM WORDGEN' or prog == 'CUSTOM':
        y.CustNewFam()
    elif prog == 'WORDGEN':
        y.NewFam()
    elif prog == 'CONVERSION':
        z.InSto()
    elif prog == 'CONJUGATE':
        z.Conjugate()
    elif prog == 'ALPHABET':
        z.Alpha()
    else:
        print('\nWomps\n')
