def readfile(filename):
    f = open(filename, encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def countlines(text):
    tolstoy = []
    textlines = text.splitlines()
    amount_of_lines = len(textlines)
    for line in textlines:
        if line.count('.') == 1 and line.endswith('.') or line.count('.') == 0:
            tolstoy.append(line)
    one_sent_lines = len(tolstoy)
    part = one_sent_lines / amount_of_lines * 100
    return part

def findstrings(text):
    while True:
        cap = input('Введите одну кириллическую заглавную букву: ')
        if cap.isupper():
            break
        else:
            print('Клавиша Caps Lock этажом выше, ты ошибся буквой, дружок-пирожок!')
    textlines = text.splitlines()
    list_of_catchwords = []
    good_catchwords = []
    for line in textlines:
        if line.startswith('—'):
            list_of_catchwords.append(line)
    for elem in list_of_catchwords:
        elem = elem.strip('— ')
        if elem.startswith(cap):
            good_catchwords.append(elem)
    if len(good_catchwords) == 0:
        print('Вращайте барабан, такой буквы здесь нет!')
    else:
        for i in range(len(good_catchwords)):
            print('— ', good_catchwords[i])

def findwords(text):
    wordlist = []
    textwordlist = []
    while True:
        word = input('Введите слово: ')
        if word != '':
            wordlist.append(word)
        if word == '':
            break
    x = len(wordlist)
    trashsigns = '.,»:;!?«'
    textwords = text.split()
    for word in textwords:
        cleanword = word.strip(trashsigns)
        if cleanword != '':
            textwordlist.append(cleanword)
    for word in wordlist:
        print(word, ':', textwordlist.count(word))

def main():
    book = readfile(r'prilepin.txt')
    percent = countlines(book)
    print(percent, '%')
    findstrings(book)
    findwords(book)

if __name__ == '__main__':
    main()
    
            
    
        
