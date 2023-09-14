Imiona = []

while True:
    Pytanie = input('Wpisz imię: ')
    Imiona.append(Pytanie)
    while True:
        Pytanie2 = input('Jeżeli chcesz przerwać program napisz STOP. Jeżeli dalej chcesz wypisywać imiona napisz DALEJ: ')
        choice = ['DALEJ', 'dalej']
        choice2 = ['STOP', 'stop']
        choice3 = Pytanie2 in choice
        choice4 = Pytanie2 in choice2
        choice5 = choice + choice2
        choice6 = Pytanie2 in choice5
        if choice3 is True:
            break
    
        if choice4 is True:
            for i in Imiona:
                print(i)
            print('Ilość imion: ', len(Imiona))
            break
        if choice6 is False:
            continue

    if choice4 is True:
        break
    else:
        continue
    
    

koniec = input()