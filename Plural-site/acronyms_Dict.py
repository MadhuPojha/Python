# DICTIONARY in PYTHON

acronyms = {
    'LOL' : 'laugh out loud',
    'IDK' : 'I dont know',
    'TBH' : 'to be honest'
}
sentence = 'IDK' + ' what happend ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('Sentence:', sentence)
print('Translation:', translation)