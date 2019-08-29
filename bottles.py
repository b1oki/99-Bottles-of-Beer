#!python3
# coding: utf-8
import gettext

es = gettext.translation('bottles', localedir='locales')
es.install()
_ = es.gettext


def get_bottle_word_ru(beerNum):
    if beerNum % 10 == 1 and beerNum != 11:
        word = _('бутылка')
    elif 0 < beerNum < 5:
        word = _('бутылки')
    else:
        word = _('бутылок')
    return word


for bottles in range(99, 0, -1):
    print(bottles, get_bottle_word_ru(bottles), _('пива на стене'))
    print(bottles, get_bottle_word_ru(bottles), _('пива!'))
    print(_('Возьми одну, пусти по кругу'))
print(_('Нет бутылок пива на стене'))
