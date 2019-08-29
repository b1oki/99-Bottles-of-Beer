# 99 Bottles of Beer
 
## Translation

### Generation
 
`xgettext -j -s -d bottles -o locales/ru/LC_MESSAGES/bottles.po bottles.py`

### Compilation

`msgfmt -o locales/ru/LC_MESSAGES/bottles.mo locales/ru/LC_MESSAGES/bottles`
