import text_procesing
# wygenerowanie struktur
hamlet_unique = text_procesing.unique_words('hamlet.txt')
hamlet_count = words_counter('hamlet.txt')

makbet_unique = text_procesing.unique_words('makbet.txt')
makbet_count = words_counter('makbet.txt')

otello_unique = text_procesing.unique_words('otello.txt')
otello_count = words_counter('otello.txt')
# wypisanie liczby wyrazow uzytych w pliku
print('W pliku {file} uzyto: {amount} slow'.format(file='hamlet.txt',amount=str(len(hamlet_unique))))
print('W pliku {file} uzyto: {amount} slow'.format(file='makbet.txt',amount=str(len(makbet_unique))))
print('W pliku {file} uzyto: {amount} slow'.format(file='otello.txt',amount=str(len(otello_unique))))
#  wspolne wyrazy
hamlet_makbet_common = 0
hamlet_otello_common = 0
makbet_otello_common = 0
for word in hamlet_unique:
    if word in makbet_unique:
        hamlet_makbet_common += 1

for word in hamlet_unique:
    if word in otello_unique:
        hamlet_otello_common += 1

for word in makbet_unique:
    if word in otello_unique:
        makbet_otello_common += 1

print('Ilosc wspolnych wyrazow dla plikow {file1} i {file2} : {number}'.format(file1='hamlet.txt',file2='makbet.txt',number=str(hamlet_makbet_common)))
print('Ilosc wspolnych wyrazow dla plikow {file1} i {file2} : {number}'.format(file1='hamlet.txt',file2='otello.txt',number=str(hamlet_otello_common)))
print('Ilosc wspolnych wyrazow dla plikow {file1} i {file2} : {number}'.format(file1='makbet.txt',file2='otello.txt',number=str(makbet_otello_common)))
