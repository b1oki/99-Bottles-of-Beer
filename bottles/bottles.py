#!python3
# coding: utf-8
import gettext


def init_gettext() -> classmethod:
    es = gettext.translation('bottles', localedir='bottles/locales')
    es.install()
    _ = es.gettext
    return _


def get_bottle_word_ru(beer_num: int) -> str:
    if beer_num % 10 == 1 and beer_num != 11:
        word = _('бутылка')
    elif 0 < beer_num < 5:
        word = _('бутылки')
    else:
        word = _('бутылок')
    return word


def print_song():
    for bottles in range(99, 0, -1):
        print(bottles, get_bottle_word_ru(bottles), _('пива на стене'))
        print(bottles, get_bottle_word_ru(bottles), _('пива!'))
        print(_('Возьми одну, пусти по кругу'))
    print(_('Нет бутылок пива на стене'))


if __name__ == '__main__':
    _ = init_gettext()
    print_song()
