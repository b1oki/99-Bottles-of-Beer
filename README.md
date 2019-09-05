# 99 Bottles of Beer
 
## Translation

### Generation
 
`xgettext -j -s -d bottles -o bottles/locales/ru/LC_MESSAGES/bottles.po bottles/bottles.py`

### Compilation

`msgfmt -o bottles/locales/ru/LC_MESSAGES/bottles.mo bottles/locales/ru/LC_MESSAGES/bottles`
