# 99 Bottles of Beer
 
## Translation

### Generation
 
`xgettext -j -s -d base -o locales/ru/LC_MESSAGES/base.po bottles.py`

### Compilation

`msgfmt -o locales/ru/LC_MESSAGES/base.mo locales/ru/LC_MESSAGES/base`
