'''
Module is about check variety of vocabulary in files

Extended description here.
'''
import string
def unique_words(input):
    '''
    Returns list of unique words within the file

    Unique words are lower case and prepared to count
    '''
    f = open('{file}'.format(file=input),'r')
    exclude = set(string.punctuation)
    unique = []
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            word = ''.join(ch for ch in word if ch not in exclude)
            word = word.lower()
            if word in unique:
                pass
            else:
                unique.append(word)
    f.seek(0)
    return unique

def words_counter(input):
    '''
    Returns dictionary containing data in form 'word': word_count

    Extended description
    '''
    f = open('{file}'.format(file=input),'r')
    word_list = unique_words(input)
    word_count = {}
    exclude = set(string.punctuation)
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            word = ''.join(ch for ch in word if ch not in exclude)
            word = word.lower()
            if word not  in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    return word_count
