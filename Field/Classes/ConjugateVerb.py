class ConjugateVerb():

    def __init__(self):
        #Setup
        #I/He/She/They(sing.), You, Ya'll/Them/They(plur), We(royal), We(exclusive)
        self.PresEndings = [ 'aj','ast','asta','am','ama' ]
        self.PastEndings = [ 'a','as','asa','an','ana' ]
        self.FutureEndings = [ 'ua','ue','ust','un','una' ]
        self.PresProgEndings = [ 'aja','asta','ast','ama','am' ]
        self.PastProgEndings = [ 'ag','asa','as','ana','an' ]
        self.FutureProgEndings = [ 'ui','ust','ue','una','un' ]
        self.O = 'I/He/She/They(sing): '
        self.I = 'You: '
        self.II = "Ya'll/Them/They(plur): "
        self.III = 'We(royal): '
        self.IV = 'We(exclusive): '


    def Conjugate(self):
        verb = input('Verb: ')
        verb = verb.upper()
        tense = input('Tense: ')
        tense = tense.upper()
        if 'PRESENT' in tense:
            print(self.O + self.PresEndings[0])
            print(self.I + self.PresEndings[1])
            print(self.II + self.PresEndings[2])
            print(self.III + self.PresEndings[3])
            print(self.IV + self.PresEndings[4])
        elif 'PAST' in tense:
            print(self.O + self.PastEndings[0])
            print(self.I + self.PastEndings[1])
            print(self.II + self.PastEndings[2])
            print(self.III + self.PastEndings[3])
            print(self.IV + self.PastEndings[4])
        elif 'FUTURE' in tense:
            print(self.O + self.FutureEndings[0])
            print(self.I + self.FutureEndings[1])
            print(self.II + self.FutureEndings[2])
            print(self.III + self.FutureEndings[3])
            print(self.IV + self.FutureEndings[4])
        elif 'PRESENT PROGRESSIVE' in tense:
            print(self.O + self.PresProgEndings[0])
            print(self.I + self.PresProgEndings[1])
            print(self.II + self.PresProgEndings[2])
            print(self.III + self.PresProgEndings[3])
            print(self.IV + self.PresProgEndings[4])
        elif 'PAST PROGRESSIVE' in tense:
            print(self.O + self.PastProgEndings[0])
            print(self.I + self.PastProgEndings[1])
            print(self.II + self.PastProgEndings[2])
            print(self.III + self.PastProgEndings[3])
            print(self.IV + self.PastProgEndings[4])
        elif 'FUTURE PROGRESSIVE' in tense:
            print(self.O + self.FutureProgEndings[0])
            print(self.I + self.FutureProgEndings[1])
            print(self.II + self.FutureProgEndings[2])
            print(self.III + self.FutureProgEndings[3])
            print(self.IV + self.FutureProgEndings[4])
