import text_procesing
from collections import OrderedDict
from operator import itemgetter
def most_common(slownik, n):
    '''
    Sorts dictionary by word_counts and print 10 most common words

    Extended description
    '''

    sorted_dict = OrderedDict(sorted(slownik.items(), key = itemgetter(1), reverse = True))
    lista = [(k,v) for k,v in sorted_dict.items()]
    most_common_words = []
    for i in range(n):
        most_common_words.append(lista[i])
    return most_common_words

hamlet_most_common = most_common(text_procesing.words_counter('hamlet.txt'),10)
makbet_most_common = most_common(text_procesing.words_counter('makbet.txt'),10)
otello_most_common = most_common(text_procesing.words_counter('otello.txt'),10)
# wyswietlenie 3 kolumny pod 10 wierszy
print('{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(*hamlet_most_common))
print('{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(*makbet_most_common))
print('{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(*otello_most_common))
