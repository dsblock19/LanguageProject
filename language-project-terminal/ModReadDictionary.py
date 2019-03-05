#MOD: takes input and reads entry based on input

def GetDictionary(word, lines):
    i = lines.index(word) + 1
    while True:
        if lines[i] == '*******':
            break
        else:
            i += 1
    return lines[lines.index(word) + 1:i]

def ReadDictionary():
    with open('/home/pi/Desktop/ConlangDatabase.txt', 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    while True:
        word = input('word?: ')
        print('\n'.join(GetDictionary(word, lines)))
        print(' ')
        break
    