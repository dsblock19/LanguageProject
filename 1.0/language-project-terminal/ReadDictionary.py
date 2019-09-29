#takes input and reads entry based on input

def ReadDictionary(word, lines):
    i = lines.index(word) + 1
    while True:
        if lines[i] == '*******':
            break
        else:
            i += 1
    return lines[lines.index(word) + 1:i]

with open('/home/pi/Desktop/ConlangDatabase.txt', 'r') as f:
    lines = [line.replace('\n', '') for line in f.readlines()]

while True:
    word = input('word?: ')
    print('\n'.join(ReadDictionary(word, lines)))
    print(' ')
    break
    