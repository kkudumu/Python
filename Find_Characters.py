word_list = ['july', 'june', 'month', 'day']
char = set('u')
  
def finder():
    for word in word_list:
        if char & set(word):
            print word


finder()