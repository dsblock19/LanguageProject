class GrammarVars():
    #lists of all avalible sounds to the language
    core_consonants = [ 'd', 't', 'c', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'sh', 'x', 'th', 'st', 'v', 'j', 'ch', 'b', 'h', 'r' ]
    core_vowels = [ 'aw', 'o', 'i', 'u', 'a', 'i:i', 'oo' ]
    allsounds = core_consonants + core_vowels

    #lists of possible endings avalible to the language
    verb_ending = 't'
    n_classI = [ 'i:i', 'aw', 'a' ]
    n_classII = [ 'c', 'k', 'x' ]
    n_classIII = [ 'st', 'th' ]
    n_classIV = [ 'ms', 'm', 'i' ]
    n_classV = [ 'o', 'e', 'ipa' ]
    n_classVI = [ 'd', 'z', 'n', 'g', 'p', 'b' ]

    # avalible sounds in language
    core_consonants = ( 'd', 't', 'k', 'z', 'n', 's', 'm', 'g', 'p', 'v', 'j', 'b', 'h', 'r' )
    core_vowels = ( 'aw', 'o', 'u', 'a', 'oo', 'e' )
    other_vowels = ( 'i:i', 'i' )
    other_consonants = ( 'c', 'sh', 'th', 'st', 'ch', 'x' )
    other_c = ( 'qua' )
    all_vowels = core_vowels + other_vowels
    all_consonants = core_consonants + other_consonants
    allsounds = core_consonants + core_vowels + other_vowels + other_consonants

    # endings to classify word as verb or noun and which class of verb/noun
    RV = ('t')
    NI = ( 'i:i', 'aw', 'a' )
    NII = ( 'c', 'k', 'x' )
    NIII = ( 'st', 'th' )
    NIV = ( 'ms', 'm', 'i' )
    NV = ( 'o', 'e', 'ipa' )
    NVI = ( 'd', 'z', 'n', 'g', 'p', 'b' )

    # pronoun groups
    ProI = 'I/He/She/They(sing): '
    ProII = 'You: '
    ProIII = 'Yall/They(plural): '
    ProIV = 'We(royal): '
    ProV = 'We(exclusive): '

    # VERB ENDINGS
    #present
    PrPI = 'taj'
    PrPII = 'tast'
    PrPIII = 'tasta'
    PrPIV = 'tam'
    PrPV = 'tama'
    #past
    PaPI = 'ta'
    PaPII = 'tas'
    PaPIII = 'tasa'
    PaPIV = 'tan'
    PaPV = 'tana'
    #future
    FuPI = 'tua'
    FuPII = 'tue'
    FuPIII = 'tust'
    FuPIV = 'tun'
    FuPV = 'tuna'
    #present progressive
    PrPgPI = 'taja'
    PrPgPII = 'tasta'
    PrPgPIII = 'tast'
    PrPgPIV = 'tama'
    PrPgPV = 'tam'
    #past progressive
    PaPgPI = 'tag'
    PaPgPII = 'tasa'
    PaPgPIII = 'tas'
    PaPgPIV = 'tana'
    PaPgPV = 'tan'
    #future progressive
    FuPgPI = 'tui'
    FuPgPII = 'tust'
    FuPgPIII = 'tue'
    FuPgPIV = 'tuna'
    FuPgPV = 'tun'

    # NOUN DECLINATION
    #PREFIXES
    #nominal number
    Sing = 'ia'
    Tri = 'io'
    Pau = 'i'
    #case
    Vdative = ('m', 'n')
    Cdative = ('ma', 'na')
    instrumental = 'st'
    comitative = 'u'
    adesive = 'za'
    allative = 'zi'
    ablative = 'zo'
    illative = 'thi'
    inessive = 'tho'
    #SUFFIXES
    #case
    acusative = ('m', 'ma', 'n', 'na')
    genitive = 'a'
    locative = ('ga', 'gua')
