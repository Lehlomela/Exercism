ALPHABETS = 'qwertyuiopasdfghjklzxcvbnm'


def is_pangram(sentence):

    for x in ALPHABETS:
        if x not in sentence.lower():
            return False

    return True