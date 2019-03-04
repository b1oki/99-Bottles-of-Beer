def get_bottle_word_ru(beerNum):
    if beerNum % 10 == 1 and beerNum != 11:
    	word = 'бутылка'
    elif 0 < beerNum < 5:
        word = 'бутылки'
    else:
    	word = 'бутылок'
    return word

for bottles in range(99, 0, -1):
    print(bottles,get_bottle_word_ru(bottles),'пива на стене')
    print(bottles,get_bottle_word_ru(bottles),'пива!')
    print('Возьми одну, пусти по кругу')
print('Нет бутылок пива на стене')
