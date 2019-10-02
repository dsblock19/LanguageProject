#takes input for word and tense (if verb) and reads entry based on input

def GetDictionary(word, lines):
    if word.endswith('t') is True:
        tense = input('Tense?: ')
        if tense in ['present']:
            i = lines.index(word) + 4
            while True:
                if lines[i] == '* ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 4:i]
        elif tense in ['past']:
            i = lines.index(word) + 11
            while True:
                if lines[i] == '** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 11:i]
        elif tense in ['future']:
            i = lines.index(word) + 18
            while True:
                if lines[i] == '*** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 18:i]
        elif tense in ['Present Progressive']:
            i = lines.index(word) + 25
            while True:
                if lines[i] == '**** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 25:i]
        elif tense in ['Past Progressive']:
            i = lines.index(word) + 32
            while True:
                if lines[i] == '***** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 32:i]
        elif tense in ['Future Progressive']:
            i = lines.index(word) + 39
            while True:
                if lines[i] == '****** ':
                    break
                else:
                    i += 1
            return lines[lines.index(word) + 39:i]
    else:
        i = lines.index(word) + 5
        while True:
            if lines[i] == '*******':
                break
            else:
                i += 1
        return lines[lines.index(word) + 5:i]

def Dictionary():
    with open('/home/pi/Desktop/MyCode/LanguageProject/Output/ConlangDatabase.txt', 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    while True:
        word = input('word?: ')
        i = lines[lines.index(word) + 1]
        print(''.join(i))
        print('\n'.join(GetDictionary(word, lines)))
        print(' ')
